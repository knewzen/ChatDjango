# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
# Create your models here.
class People(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    nickName = models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    message = models.CharField(max_length=140)
    created = models.DateTimeField(auto_now = True)
    update  = models.DateTimeField(auto_now_add = True)
