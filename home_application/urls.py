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

from django.conf.urls import patterns

urlpatterns = patterns(
    'home_application.views',
    (r'^$', 'home'),
    (r'^submit_template/$', 'submit_template'),
    (r'^dev-guide/$', 'dev_guide'),
    (r'^contactus/$', 'contactus'),
    # (r'^tijiao/$', 'tijiao'),
    # # 作业二
    # (r'^host_disk/$', 'host_disk'),
    # (r'^host_tijiao/$', 'host_tijiao'),
    #
    # (r'^host_script/$', 'host_script'),
    # (r'^script_tijiao/$', 'script_tijiao'),
    #
    # # 其他
    # (r'^other/$', 'other'),
    # # ##文件上传
    # (r'^other/upload_file/$', 'upload_file'),
    # # ## 文件下载
    # (r'^other/download/$', 'download_file'),

    # 模拟考试1
    # ## 首页
    (r'^mock_exam1/upload_file/$', 'mock_exam1_upload_file'),
    # ## 执行按钮
    (r'^mock_exam/exec_job/$', 'mock_exam1_exec_job'),
    # ## 执行记录页面
    (r'^mock_exam/exec_log/$', 'mock_exam1_exec_log'),
    # ## 显示日志
    (r'^mock_exam/show_log/$', 'mock_exam1_show_log'),
)
