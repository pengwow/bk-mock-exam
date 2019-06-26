# coding=utf-8
from django.shortcuts import render
from django.forms.models import model_to_dict
from common.mymako import render_mako_context, render_json
from blueking.component.shortcuts import get_client_by_request
from django.views.decorators.csrf import csrf_exempt
from models import TaskWaitData, TaskWaitMaster
import xlrd
import json


def not_null(data):
    if data and u'null' != data.lower():
        return True
    else:
        return False


# Create your views here.
def home(request):
    """
    首页
    :param request:
    :return:
    """
    data = request.GET
    query_dict = dict()
    if not_null(data.get('bk_biz_id')):
        query_dict['bk_biz_id'] = data.get('bk_biz_id')
    if not_null(data.get('modal_template_name')):
        query_dict['modal_template_name'] = data.get('modal_template_name')
    if not_null(data.get('bk_type_modal')):
        query_dict['bk_type_modal'] = data.get('bk_type_modal')
    if not_null(data.get('modal_identifier')):
        query_dict['modal_identifier'] = data.get('modal_identifier')
    if not_null(data.get('user')):
        query_dict['user'] = data.get('user')
    if not_null(data.get('status')):
        query_dict['status'] = data.get('status')

    # 从环境配置获取APP信息，从request获取当前用户信息
    client = get_client_by_request(request)
    # 获取业务
    kwargs = {}
    result = client.cc.search_business(kwargs)
    business = result['data']['info']
    # bk_biz_id bk_biz_name

    kwargs = {}
    result = client.bk_login.get_all_users(kwargs)
    user_list = result['data']

    # 读取待办数据
    if not query_dict:
        taskwait = TaskWaitMaster.objects.all()
    else:
        taskwait = TaskWaitMaster.objects.filter(**query_dict)
    wait_list = list()
    for item in taskwait:
        wait_list.append(dict(
            template_name=item.modal_template_name,
            identifier=item.modal_identifier,
            template_biz_name=item.bk_biz_name,
            template_type=item.bk_type_modal,
            user=item.user,
            create_date=item.create_time,
            status=item.status,
            wait_id=item.id
        ))

    return render_mako_context(request,
                               '/mock_exam2/mock_exam2_index.html',
                               {"business": business,
                                "wait_list": wait_list,
                                "user_list": user_list})


@csrf_exempt
def create_task(request):
    """
    创建任务
    :param request:
    :return:
    """
    # 接收表单数据
    bk_biz_id = request.POST.get('bk_biz_id')
    bk_biz_name = request.POST.get('bk_biz_name')
    modal_template_name = request.POST.get('modal_template_name')
    bk_type_modal = request.POST.get('bk_type_modal')
    modal_identifier = request.POST.get('modal_identifier')

    # 接收的为文件列表，需要遍历操作
    files = request.FILES
    for item in files:
        temp_dict = dict()
        _file = files.get(item)
        temp_dict['bk_biz_id'] = bk_biz_id
        temp_dict['bk_biz_name'] = bk_biz_name
        temp_dict['modal_template_name'] = modal_template_name
        temp_dict['bk_type_modal'] = bk_type_modal
        temp_dict['modal_identifier'] = modal_identifier
        temp_dict['user'] = request.user.username
        temp_dict['status'] = '待操作'
        task_master = TaskWaitMaster(**temp_dict)
        task_master.save()

        data = xlrd.open_workbook(file_contents=_file.file.read())
        table = data.sheets()[0]
        nrows = table.nrows
        for i in range(1, nrows):
            temp_dict2 = dict()
            temp_dict2['master_id'] = task_master.id
            temp_dict2['sequence'] = table.row_values(i)[0]
            temp_dict2['operational'] = table.row_values(i)[1]
            temp_dict2['remark'] = table.row_values(i)[2]
            temp_dict2['liable'] = table.row_values(i)[3]
            temp_dict2['status'] = '未完成'
            taskfiler = TaskWaitData(**temp_dict2)
            taskfiler.save()
    return render_json("OK")


def exec_wait_page(request):
    """
    待办操作页面
    :param request:
    :return:
    """
    wait_id = request.GET.get('wait_id')
    task_data = TaskWaitData.objects.filter(master_id=wait_id)
    wait_list = list()
    for item in task_data:
        model_dict = model_to_dict(item)
        if '完成' != model_dict['status']:
            model_dict['is_exec'] = True
        else:
            model_dict['is_exec'] = False
        wait_list.append(model_dict)
    return render_mako_context(request,
                               '/mock_exam2/mock_exam2_exec.html',
                               {'wait_list': wait_list}
                               )


def exec_wait(request):
    data = json.loads(request.body)
    exec_id = data.get('exec_id')
    task = TaskWaitData.objects.get(id=exec_id)
    task.status = '完成'
    task.save()
    master_task = TaskWaitData.objects.filter(master_id=task.master_id, status='未完成')
    task = TaskWaitMaster.objects.get(id=task.master_id)
    task.status = '操作中'

    if not len(master_task):
        task.status = '已完成'
    task.save()
    return render_json("OK")


def query_data(request):
    data = json.loads(request.body)
    query_dict = dict()
    if data.get('bk_biz_id'):
        query_dict['bk_biz_id'] = data.get('bk_biz_id')
    if data.get('modal_template_name'):
        query_dict['modal_template_name'] = data.get('modal_template_name')
    if data.get('bk_type_modal'):
        query_dict['bk_type_modal'] = data.get('bk_type_modal')
    if data.get('modal_identifier'):
        query_dict['modal_identifier'] = data.get('modal_identifier')
    if data.get('user'):
        query_dict['user'] = data.get('user')
    if data.get('status'):
        query_dict['status'] = data.get('status')

    # 从环境配置获取APP信息，从request获取当前用户信息
    client = get_client_by_request(request)
    # 获取业务
    kwargs = {}
    result = client.cc.search_business(kwargs)
    business = result['data']['info']
    # bk_biz_id bk_biz_name

    # 读取待办数据
    taskwait = TaskWaitMaster.objects.filter(**query_dict)
    wait_list = list()
    for item in taskwait:
        wait_list.append(dict(
            template_name=item.modal_template_name,
            identifier=item.modal_identifier,
            template_biz_name=item.bk_biz_id,
            template_type=item.bk_type_modal,
            user=item.user,
            create_date=item.create_time,
            status=item.status,
            wait_id=item.id
        ))
    return render_mako_context(request,
                               '/mock_exam2/mock_exam2_index.html',
                               {"business": business,
                                "wait_list": wait_list})
