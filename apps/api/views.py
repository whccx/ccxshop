# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from shop.models import Goodsinfo,Goodsparameter
from api.serializers import GoodsinfoSerializer,GoodsparameterSerializer,UserSerializer
from rest_framework import permissions,viewsets
from api.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User

from api.filter import Goodsinfofilter,Goodsparameterfilter
from django_filters.rest_framework import DjangoFilterBackend

#============================================================================
# 开始.GoodsinfoViewSet
class GoodsinfoViewSet(viewsets.ModelViewSet):
    """
    此视图自动提供`list`，`create`，`retrieve`，`update`和`destroy`操作。
    """
    queryset = Goodsinfo.objects.all()
    serializer_class = GoodsinfoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    #使用过滤器
    filter_backends = (DjangoFilterBackend,)
    #定义需要使用过滤器的字段
    #filter_fields = ['name',]
    filter_class = Goodsinfofilter
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

#=======================================================================
# 开始.GoodsparameterViewSet
class GoodsparameterViewSet(viewsets.ModelViewSet):
    """
    此视图自动提供`list`，`create`，`retrieve`，`update`和`destroy`操作。
    """
    queryset = Goodsparameter.objects.all()
    serializer_class = GoodsparameterSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    # 使用过滤器
    filter_backends = (DjangoFilterBackend,)
    # 定义需要使用过滤器的字段
    # filter_fields = ['name',]
    filter_class = Goodsparameterfilter
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

#====================================================================
# 开始.UserViewSet
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    此视图自动提供`list`和`detail`操作。
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
