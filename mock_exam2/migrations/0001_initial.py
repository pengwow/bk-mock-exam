# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mock_exam2.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskWaitData',
            fields=[
                ('id', models.CharField(default=mock_exam2.models.get_uuid, max_length=36, serialize=False, primary_key=True)),
                ('master_id', models.CharField(max_length=64)),
                ('sequence', models.CharField(max_length=10)),
                ('operational', models.CharField(max_length=255)),
                ('remark', models.CharField(max_length=255)),
                ('liable', models.CharField(max_length=64)),
                ('completion_time', models.CharField(max_length=64)),
                ('confirmer', models.CharField(max_length=64)),
                ('status', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'task_wait_data',
            },
        ),
        migrations.CreateModel(
            name='TaskWaitMaster',
            fields=[
                ('id', models.CharField(default=mock_exam2.models.get_uuid, max_length=36, serialize=False, primary_key=True)),
                ('bk_biz_id', models.CharField(max_length=64)),
                ('bk_biz_name', models.CharField(max_length=64)),
                ('modal_template_name', models.CharField(max_length=64)),
                ('bk_type_modal', models.CharField(max_length=64)),
                ('modal_identifier', models.CharField(max_length=64)),
                ('user', models.CharField(max_length=64)),
                ('create_time', models.CharField(default=b'2019-06-25 17:03:34.578000', max_length=64)),
                ('status', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'task_wait_master',
            },
        ),
    ]
