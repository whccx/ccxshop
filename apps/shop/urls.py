# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import path,include
from shop import serializers,views #导入py文件
app_name = 'shop'

from rest_framework import routers

#REST路由
router = routers.DefaultRouter()
router.register('goods', serializers.ShopViewSet)

urlpatterns = [
    path('goods', views.goods_list),#全部展示
    path('goods/(?P<pk>[0-9]+)/', views.goods_detail),#指定id
    path('', include(router.urls)),#默认shop页面
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), #Web API
]