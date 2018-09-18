# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20,default="",verbose_name="类别名字")
    level = models.IntegerField(default=0,verbose_name="类别层级")
    parent_id = models.IntegerField(default=1,verbose_name="父级ID")
    path = models.CharField(max_length=20,default="",verbose_name="类别路径")

    class Meta:
        verbose_name = "全部分类"