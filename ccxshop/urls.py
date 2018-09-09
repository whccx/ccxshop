# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#网站ico
from django.views.generic.base import RedirectView

from django.urls import path,include
from django.contrib import admin

from . import views

urlpatterns = [
    path('favicon.ico',RedirectView.as_view(url='static/favicon.ico')),#网站icon
    path('admin/', admin.site.urls),#后台
    path('', views.index), #首页
    path('shop/', include('shop.urls',namespace='shop')),#商品app链接
]


