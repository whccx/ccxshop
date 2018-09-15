# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url,include
from shop import views #导入py文件

app_name = 'shop'

urlpatterns = [
	url(r'^$', views.shop),#默认shop页面
]