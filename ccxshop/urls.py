# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#网站ico
from django.views.generic.base import RedirectView
from django.conf.urls import url,include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^favicon.ico$',RedirectView.as_view(url='static/favicon.ico')),#网站icon
    url(r'^admin/', admin.site.urls),#后台
    url(r'^tinymce/', include('tinymce.urls')),#富文本编辑器

    url(r'^$',  views.index),#首页
    url(r'^shop/', include('shop.urls')),#商品url

    url(r'^api/$', views.api), #api
    url(r'^api/shop/', include('shop.apiurls')), #商品api

]


