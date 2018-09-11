# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url,include
from shop import views #导入py文件
from rest_framework.urlpatterns import format_suffix_patterns
app_name = 'shop'

urlpatterns = [
    url(r'^$', views.shopin),#默认shop页面
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')), #Web API
    url(r'^goods/$', views.GoodsList.as_view()),
    url(r'^goods/(?P<pk>[0-9]+)$', views.GoodsDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)