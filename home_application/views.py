# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""

from common.mymako import render_mako_context, render_json
from blueking.component.shortcuts import get_client_by_request
from django.views.decorators.csrf import csrf_exempt
from models import TaskFileR, JobLogTaskR
from django.forms.models import model_to_dict
import json
import base64


def home(request):
    """
    首页
    """
    bk_biz_id = request.GET.get('bk_biz_id')
    # 从环境配置获取APP信息，从request获取当前用户信息
    client = get_client_by_request(request)
    # 获取业务
    kwargs = {}
    result = client.cc.search_business(kwargs)
    business = result['data']['info']
    # 如果前端带着id
    if bk_biz_id:
        # 如果前端带着业务id，则进行查找，把查询的业务数据提前
        for item in range(len(business)):
            if str(bk_biz_id) == str(business[item]['bk_biz_id']):
                find_bk_biz_id = business.pop(item)
                business.insert(0, find_bk_biz_id)
                break
    else:
        # 如果id未知，则默认第一个业务id
        bk_biz_id = business[0]['bk_biz_id']

    taskfiler = TaskFileR.objects.all()
    task_list = list()
    for item in taskfiler:
        task_list.append(model_to_dict(item))

    # 获取主机
    kwargs = {}
    kwargs['bk_biz_id'] = bk_biz_id
    result = client.cc.search_host(kwargs)
    host_list = result['data']['info']
    re_host_list = list()
    for item in host_list:
        re_host_list.append(dict(bk_host_innerip=item['host']['bk_host_innerip'],
                                 bk_os_name=item['host']['bk_os_name'],
                                 bk_os_version=item['host']['bk_os_version'],
                                 bk_host_id=item['host']['bk_host_id']
                                 ))
    return render_mako_context(request, '/home_application/home.html',
                               {
                                   "business": business,
                                   "task_list": task_list,
                                   "host_list": re_host_list
                               })


def submit_template(request):
    """
    首页
    """
    print(request.body)
    return render_json({"1111111": "dddddddddd"})


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')


# def tijiao(request):
#     data = json.loads(request.body)
#     print(type(data))
#     sss = TEST(**data)
#     sss.save()
#     return render_json({"DATA": "AAAAAAAA"})
#
#
# def host_disk(request):
#     host_list = HostDisk.objects.all()
#     re_list = list()
#     for item in host_list:
#         temp_dict = dict()
#         temp_dict['os'] = item.os
#         temp_dict['host_ip'] = item.host_ip
#         temp_dict['host_name'] = item.host_name
#         temp_dict['host_path'] = item.host_path
#         temp_dict['create_time'] = item.create_time
#         re_list.append(temp_dict)
#
#     print(re_list)
#     return render_mako_context(request,
#                                '/home_application/host_disk.html',
#                                {'host_all': re_list}
#                                )
#
#
# def host_tijiao(request):
#     data = request.body
#     print(type(data))
#     data = json.loads(data)
#
#     host = HostDisk(**data)
#     host.save()
#     return render_json({"status": "OK"})
#
#
# def host_script(request):
#     # 根据作业id查询日志
#     data = ScriptExecInfo.objects.all()
#     client = get_client_by_request(request)
#     script_all = list()
#     for item in data:
#         temp_dict = dict()
#         kwargs = {}
#         kwargs['bk_biz_id'] = item.bk_biz_id
#         kwargs['job_instance_id'] = item.job_instance_id
#         result = client.job.get_job_instance_log(kwargs)
#         log_content = result['data'][0]['step_results'][0]['ip_logs'][0]['log_content']
#         temp_dict['host_ip'] = item.host_ip
#         temp_dict['log_content'] = log_content
#         temp_dict['script_content'] = item.script_content
#         temp_dict['create_time'] = item.create_time
#         script_all.append(temp_dict)
#
#     return render_mako_context(request,
#                                '/home_application/host_script.html',
#                                {'script_all': script_all},
#                                )
#
#
# def script_tijiao(request):
#     try:
#         print(request.user.username)
#     except Exception as e:
#         print(str(e))
#     data = json.loads(request.body)
#     client = get_client_by_request(request)
#     kwargs = {}
#     result = client.cc.search_business(kwargs)
#     bk_biz_id = result['data']['info'][0]['bk_biz_id']
#
#     script_content = base64.b64encode(data['script_content'])
#     kwargs = dict()
#     kwargs['bk_biz_id'] = bk_biz_id
#     kwargs['script_content'] = script_content
#     kwargs["account"] = "root"
#     kwargs['ip_list'] = [{'bk_cloud_id': 0, "ip": data['host_ip']}]
#     result = client.job.fast_execute_script(kwargs)
#
#     script_dict = dict()
#     script_dict["host_ip"] = data['host_ip']
#     script_dict["script_content"] = data['script_content']
#     script_dict["job_instance_id"] = result['data']['job_instance_id']
#     script_dict['bk_biz_id'] = bk_biz_id
#     scriptexecinfo = ScriptExecInfo(**script_dict)
#     scriptexecinfo.save()
#
#     return render_json({"status": "OK"})
#
#
# # ####################其他
# def other(request):
#     return render_mako_context(request, '/home_application/other.html')
#
# @csrf_exempt  # 注意：需要添加此装饰器
# def upload_file(request):
#     # 接收的为文件列表，需要遍历操作
#     files = request.FILES
#     for item in files:
#         _file = files.get(item)
#         print(_file.name)
#         print(_file.size)
#         with open('./' + str(_file.name), 'wb') as fd:
#             fd.write(_file.file.read())
#     return render_json({"status": "OK"})

@csrf_exempt
def mock_exam1_upload_file(request):
    # 接收表单数据
    task_type = request.POST.get('task_type')
    # 接收的为文件列表，需要遍历操作
    files = request.FILES
    re_list = list()
    for item in files:
        temp_dict = dict()
        _file = files.get(item)
        temp_dict['task_type'] = task_type
        temp_dict['filename'] = _file.name
        temp_dict['file_content'] = _file.file.read()
        taskfiler = TaskFileR(**temp_dict)
        taskfiler.save()
        re_list.append(dict(filename=temp_dict['filename'],
                            task_type=temp_dict['task_type'],
                            id=taskfiler.id))
    return render_json(re_list)


@csrf_exempt
def mock_exam1_exec_job(request):
    param = json.loads(request.body)
    print(param)
    client = get_client_by_request(request)

    checkboxs = param.get('checkboxs')
    checkboxs = checkboxs.split(',')
    if len(checkboxs) < 1:
        return render_json("未选择主机")
    ip_list = list()
    for item in checkboxs:
        ip_list.append(dict(ip=item,
                            bk_cloud_id=0)
                       )

    taskfiler = TaskFileR.objects.get(id=param.get('task_id'))

    kwargs = {}
    kwargs['bk_biz_id'] = param.get('bk_biz_id')
    kwargs['account'] = 'root'
    kwargs['script_content'] = base64.b64encode(taskfiler.file_content)
    kwargs['script_param'] = base64.b64encode(param.get('args'))
    kwargs['ip_list'] = ip_list

    result = client.job.fast_execute_script(kwargs)
    job_instance_id = result['data']['job_instance_id']
    job_instance_name = result['data']['job_instance_name']
    # 保存数据
    joblogtaskr_dict = dict()
    joblogtaskr_dict['task_id'] = param.get('task_id')
    joblogtaskr_dict['job_instance_id'] = job_instance_id
    joblogtaskr_dict['job_instance_name'] = job_instance_name
    joblogtaskr_dict['bk_biz_id'] = kwargs['bk_biz_id']
    joblogtaskr = JobLogTaskR(**joblogtaskr_dict)
    joblogtaskr.save()

    return render_json("已启动作业：%s" % job_instance_id)


def mock_exam1_exec_log(request):
    joblogtaskr = JobLogTaskR.objects.all()
    log_list = list()
    for item in joblogtaskr:
        taskfiler = TaskFileR.objects.get(id=item.task_id)
        log_list.append(dict(
            task_type=taskfiler.task_type,
            file_content=taskfiler.file_content,
            filename=taskfiler.filename,
            job_instance_id=item.job_instance_id,
            id=item.id,
            create_time=item.create_time,
            job_instance_name=item.job_instance_name,
        ))

    return render_mako_context(request,
                               '/home_application/mock_exam1_log.html',
                               {"log_list": log_list})


@csrf_exempt
def mock_exam1_show_log(request):
    data = json.loads(request.body)
    _id = data.get('id')
    joblogtaskr = JobLogTaskR.objects.get(id=_id)

    # 获取日志
    kwargs = {}
    kwargs['bk_biz_id'] = joblogtaskr.bk_biz_id
    kwargs['job_instance_id'] = joblogtaskr.job_instance_id
    client = get_client_by_request(request)
    result = client.job.get_job_instance_log(kwargs)
    if result['data'][0]['is_finished']:
        log_content = result['data'][0]['step_results'][0]['ip_logs'][0]['log_content']
    else:
        log_content = "作业未执行完！"
    return render_json(log_content)
