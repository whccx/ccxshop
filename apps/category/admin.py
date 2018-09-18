# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from category.models import Category

# 模型的管理器
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'level', 'parent_id','path')
    list_editable = ['name', 'level', 'parent_id','path']
    list_display_links = ('id',)