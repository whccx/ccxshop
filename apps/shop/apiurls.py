# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url,include
from shop.views import GoodsinfoViewSet,GoodsparameterViewSet,UserViewSet#导入py文件
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

#===============================================================
goodsinfo_list = GoodsinfoViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

goodsinfo_detail = GoodsinfoViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

goodsinfo_highlight = GoodsinfoViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])


goodsparameter_list = GoodsparameterViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

goodsparameter_detail = GoodsparameterViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

goodsparameter_highlight = GoodsparameterViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    'get': 'list'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})
#=============================================================

urlpatterns = format_suffix_patterns([
    url(r'^goodsinfo/$', goodsinfo_list, name='goodsinfo-list'),
    url(r'^goodsinfo/(?P<pk>[0-9]+)/$', goodsinfo_detail, name='goodsinfo-detail'),
    url(r'^goodsinfo/(?P<pk>[0-9]+)/highlight/$', goodsinfo_highlight, name='goodsinfo-highlight'),
    url(r'^goodsparameter/$', goodsparameter_list, name='goodsparameter-list'),
    url(r'^goodsparameter/(?P<pk>[0-9]+)/$', goodsparameter_detail, name='goodsparameter-detail'),
    url(r'^goodsparameter/(?P<pk>[0-9]+)/highlight/$', goodsparameter_highlight, name='goodsparameter-highlight'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
])
#==================================================================

# 创建路由器并注册我们的视图。
router = DefaultRouter()
router.register(r'goodsinfo', GoodsinfoViewSet)
router.register(r'goodsparameter', GoodsparameterViewSet)
router.register(r'users', UserViewSet)

# API URL现在由路由器自动确定。
# 另外，我们还要包含可浏览的API的登录URL。
urlpatterns += [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]