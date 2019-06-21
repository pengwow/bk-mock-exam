function create_task_type() {
    let task_type = $('#task_type').val()
    let fileObj = document.getElementById("file").files[0]; // 获取文件对象
    let upload_file_url = site_url + "mock_exam1/upload_file/";                    // 接收上传文件的后台地址
    let bk_biz_id = $('#business_list').val();
    // FormData 对象
    let form = new FormData();
    form.append("task_type", task_type);                        // 可以增加表单数据
    form.append("file", fileObj);                           // 文件对象
    form.append("bk_biz_id", bk_biz_id);
    // XMLHttpRequest 对象
    let xhr = new XMLHttpRequest();
    xhr.open("post", upload_file_url, true);
    xhr.onload = function () {
        // alert("上传完成!");
    };
    xhr.send(form);
    xhr.addEventListener("load", function (e) {
        //e.target.responseText即后台返回结果
        var result = e.target.response;
        // for(var i=0; result.length()<10;i++){ //循环添加多个值
        // sid.option[i] = new Option(i,i);
        // }

        result = JSON.parse(result);
        for (var item = 0; item < result['message'].length; item++) {
            var task_type = result['message'][item]['task_type'];
            var task_id = result['message'][item]['id'];
            var app_value = "<option value='" + task_id + "'>" + task_type + "</option>";
            $('#task_list').append(app_value);
        }
        $('#myModal').modal('hide');

    }, false);
    xhr.addEventListener("error", function (e) {
        callback('error', e);
    }, false);
    xhr.addEventListener("abort", function (e) {
        callback('cancel', e);
    }, false);


}

function show_task_type() {
    $('#myModal').modal('show');
}

$(function () {
    // 切换业务列表后，重新刷新页面
    $("#business_list").change(function () {
        var data = $(this).val();
        window.location.href = site_url + '?bk_biz_id='+data
    });
});

//点击执行
function exec_job() {

    let task_id = $('#task_list').val();
    let bk_biz_id = $('#business_list').val();
    let args = $('#args').val();
    let checkboxs = $("input:checkbox[name='check']:checked").map(function (index, elem) {
        return $(elem).val();
    }).get().join(',');

    $.ajax({
        url: site_url+'mock_exam/exec_job/',
        type: 'POST',
        data:JSON.stringify({
            "task_id":task_id,
            "bk_biz_id":bk_biz_id,
            "args":args,
            "checkboxs":checkboxs
        }),
        success: function (res) {
            alert(res['message']);
        }
    });

}

function show_log(id) {

    $.ajax({
        url: site_url+'mock_exam/show_log/',
        type: 'POST',
        data:JSON.stringify({
            "id":id,
        }),
        success: function (res) {
            //alert(res['message']);
            $("#log_content").val(res['message'])
        }
    });
}
