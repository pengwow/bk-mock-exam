function create_task() {
    let bk_biz_modal = $("#bk_biz_modal").val();

    let bk_biz_name = $("#bk_biz_list option:checked").text();
    let modal_template_name = $("#modal_template_name").val();
    let modal_identifier = $("#modal_identifier").val();
    let bk_type_modal = $('#bk_type_modal').val();
    upload_file_url = site_url + 'mock_exam2/create_task/';

    let fileObj = document.getElementById("file").files[0]; // 获取文件对象
    // FormData 对象
    let form = new FormData();
    form.append("bk_biz_id", bk_biz_modal);                        // 可以增加表单数据
    form.append("bk_biz_name", bk_biz_name);
    form.append("file", fileObj);                           // 文件对象
    form.append("modal_template_name", modal_template_name);
    form.append("bk_type_modal", bk_type_modal);
    form.append("modal_identifier", modal_identifier);
    // XMLHttpRequest 对象
    let xhr = new XMLHttpRequest();
    xhr.open("post", upload_file_url, true);
    xhr.onload = function () {
        // alert("上传完成!");
    };
    xhr.send(form);
    xhr.addEventListener("load", function (e) {
        //e.target.responseText即后台返回结果
        // let result = e.target.response;
        // result = JSON.parse(result);
        // for (var item = 0; item < result['message'].length; item++) {
        //     var task_type = result['message'][item]['task_type'];
        //     var task_id = result['message'][item]['id'];
        //     var app_value = "<option value='" + task_id + "'>" + task_type + "</option>";
        //     $('#task_list').append(app_value);
        // }
        $('#myModal').modal('hide');
        window.location.href = site_url + 'mock_exam2';


    }, false);
    xhr.addEventListener("error", function (e) {
        callback('error', e);
    }, false);
    xhr.addEventListener("abort", function (e) {
        callback('cancel', e);
    }, false);


}

function exec_wait_button(wait_id) {
    window.location.href = site_url + 'mock_exam2/exec_wait_page?wait_id=' + wait_id

}

