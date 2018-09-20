# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url,include
from shop import views #导入py文件
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [    
    url(r'^goodsinfo/$', views.GoodsinfoList.as_view()),#全部商品
    url(r'^goodsinfo/(?P<pk>[0-9]+)$', views.GoodsinfoDetail.as_view()),#指定商品

    url(r'^goodsparameter/$', views.GoodsparameterList.as_view()),  # 全部商品
    url(r'^goodsparameter/(?P<pk>[0-9]+)$', views.GoodsparameterDetail.as_view()),  # 指定商品

    url(r'^users/$', views.UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
	url(r'^$', views.shopin),#默认shop页面
    url(r'^api-auth/', include('rest_framework.urls')),
]