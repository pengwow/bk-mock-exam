from django.db import models
import uuid
import datetime


def get_uuid():
    s_uuid = str(uuid.uuid1())
    l_uuid = s_uuid.split('-')
    s_uuid = ''.join(l_uuid)
    return s_uuid


# Create your models here.
class TaskWaitMaster(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=get_uuid)
    bk_biz_id = models.CharField(max_length=64)
    bk_biz_name = models.CharField(max_length=64)
    modal_template_name = models.CharField(max_length=64)
    bk_type_modal = models.CharField(max_length=64)
    modal_identifier = models.CharField(max_length=64)
    user = models.CharField(max_length=64)
    create_time = models.CharField(max_length=64, default=str(datetime.datetime.now()))
    status = models.CharField(max_length=10)

    class Meta:
        db_table = 'task_wait_master'


class TaskWaitData(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=get_uuid)
    master_id = models.CharField(max_length=64)
    sequence = models.CharField(max_length=10)
    operational = models.CharField(max_length=255)
    remark = models.CharField(max_length=255)
    liable = models.CharField(max_length=64)
    completion_time = models.CharField(max_length=64)
    confirmer = models.CharField(max_length=64)
    status = models.CharField(max_length=10)

    class Meta:
        db_table = 'task_wait_data'
