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

from django.db import models
import uuid


def get_uuid():
    s_uuid = str(uuid.uuid1())
    l_uuid = s_uuid.split('-')
    s_uuid = ''.join(l_uuid)
    return s_uuid


class TaskFileR(models.Model):
    id = models.CharField(u"主键ID", max_length=64, primary_key=True, default=get_uuid)
    task_type = models.CharField(u"业务类型", max_length=64)
    filename = models.CharField(u"脚本文件名", max_length=64)
    file_content = models.TextField(u"脚本文件内容")

    class Meta:
        db_table = 'task_file_r'


class JobLogTaskR(models.Model):
    id = models.CharField(u"主键ID", max_length=64, primary_key=True, default=get_uuid)
    task_id = models.CharField(u"业务类型", max_length=64)
    job_instance_name = models.CharField(u"作业名称", max_length=64)
    job_instance_id = models.TextField(u"作业ID")
    bk_biz_id = models.CharField(u"业务ID", max_length=64)
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)

    class Meta:
        db_table = 'job_log_task_r'

# class TEST(models.Model):
#     A = models.CharField(u"功能code", max_length=64, unique=True)
#     B = models.IntegerField(u"ss")
#     C = models.TextField()
#
#     class Meta:
#         db_table = 'lp_test'
#
#
# class HostDisk(models.Model):
#     host_name = models.CharField(max_length=64)
#     host_path = models.CharField(max_length=64)
#     os = models.CharField(max_length=64)
#     host_ip = models.CharField(max_length=64)
#     create_time = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         db_table = 'host'
#
#
# class ScriptExecInfo(models.Model):
#     script_content = models.CharField(max_length=255)
#     bk_biz_id = models.CharField(max_length=64)
#     job_instance_id = models.CharField(max_length=64)
#     host_ip = models.CharField(max_length=64)
#     create_time = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         db_table = 'script_exec_info'

##
##makemigrations
##    migrate
