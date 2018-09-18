# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
    #goods_sn = models.CharField(max_length=50, default="", verbose_name="商品唯一货号")
    name = models.CharField(max_length=20,verbose_name="类别名字")
    level = models.IntegerField(verbose_name="类别层级")
    parent_id = models.IntegerField(verbose_name="父级ID")
    #code
    #path