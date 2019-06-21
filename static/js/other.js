function UploadFile() {
    let fileObj = document.getElementById("file").files[0]; // 获取文件对象
    let upload_file_url = site_url + "other/upload_file/";                    // 接收上传文件的后台地址

    // FormData 对象
    let form = new FormData();
    form.append("author", "hooyes");                        // 可以增加表单数据
    form.append("file", fileObj);                           // 文件对象

    // XMLHttpRequest 对象
    let xhr = new XMLHttpRequest();
    xhr.open("post", upload_file_url, true);
    xhr.onload = function () {
        alert("上传完成!");
    };
    xhr.send(form);
}

function DownloadFile(filename) {
    let url = site_url + 'other/download/?filename=' + filename;
    let xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);        // 也可以使用POST方式，根据接口
    xhr.responseType = "blob";    // 返回类型blob
    // 定义请求完成的处理函数，请求前也可以增加加载框/禁用下载按钮逻辑
    xhr.onload = function () {
        // 请求完成
        if (this.status === 200) {
            // 返回200
            let blob = this.response;
            let reader = new FileReader();
            reader.readAsDataURL(blob);    // 转换为base64，可以直接放入a表情href
            reader.onload = function (e) {
                // 转换完成，创建一个a标签用于下载
                let a = document.createElement('a');
                a.download = filename;
                a.href = e.target.result;
                $("body").append(a);    // 修复firefox中无法触发click
                a.click();
                $(a).remove();
            }
        }
    };
    // 发送ajax请求
    xhr.send()
}

//分页操作
$("#jpages_demo1 .holder").jPages({
    containerID: "datas",
    previous: "←",
    next: "→",
    perPage: 10,
    delay: 10
});

//表格带参数按钮
function table_edit(table_id) {
    alert(table_id);
}

function table_delete(table_id) {
    alert(table_id);
}


//模态框显示与隐藏
function show_modal() {

    $('#myModal').modal('show');
// $('#myModal').modal('hide');
}

function hide_modal() {

    $('#myModal').modal('hide');
// $('#myModal').modal('show');
}


//复选框定位取值
function checkbox_button() {

    let text = $("input:checkbox[name='checkbox']:checked").map(function (index, elem) {
        return $(elem).val();
    }).get().join(',');
    alert("选中的checkbox的值为：" + text);

}

//单选框定位取值
function radio_button() {
    let text = $("input[name='demo-radio']:checked").val();
    alert(text);
}


//轮询相关
let int_time;
function start_time() {
    int_time = self.setInterval("clock()", 5000);
}

function clock() {
    alert('调用clock()');
}

function stop_time() {
    int_time = window.clearInterval(int_time)
}