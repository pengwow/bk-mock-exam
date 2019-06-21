# -*- coding: utf-8
from __future__ import unicode_literals

from django.apps import AppConfig


class HomeApplication(AppConfig):
    name = 'test-demo.home_application'

    def ready(self):
        with open('./123.txt','wb') as fd:
            fd.write("SSSSSSSSSSSSSSSSSSSSSSFFFFFFF#########99999430\n42354364234\nregrtas")