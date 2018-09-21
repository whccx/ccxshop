# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from shop import mixin #导入mixin.py文件
from shop.models import Goodsinfo,Goodsparameter
from shop.serializers import GoodsinfoSerializer,GoodsparameterSerializer,UserSerializer
from rest_framework import permissions,renderers,viewsets
from shop.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.decorators import detail_route
from shop.filter import Goodsinfofilter
from django_filters.rest_framework import DjangoFilterBackend
# 开始.GoodsinfoViewSet

class GoodsinfoViewSet(viewsets.ModelViewSet):
    """
    此视图自动提供`list`，`create`，`retrieve`，`update`和`destroy`操作。

    另外我们还提供了一个额外的`highlight`操作。
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

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        Goodsinfo = self.get_object()
        return Response(Goodsinfo.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

#=======================================================================

# 开始.GoodsparameterViewSet

class GoodsparameterViewSet(viewsets.ModelViewSet):
    """
    此视图自动提供`list`，`create`，`retrieve`，`update`和`destroy`操作。

    另外我们还提供了一个额外的`highlight`操作。
    """
    queryset = Goodsparameter.objects.all()
    serializer_class = GoodsparameterSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        Goodsparameter = self.get_object()
        return Response(Goodsparameter.highlighted)

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


#====================================================================

from django.shortcuts import render

def shop(request):
    """
    商品
    """
    return render(request,'shop/show.html')

#=====================================================================
#from rest_framework import mixins,viewsets
# from shop.filter import Goodsinfofilter
# from django_filters.rest_framework import DjangoFilterBackend
#
# class GoodListViewSet(generics.ListCreateAPIView):
#     queryset = Goodsinfo.objects.all()
#     serializer_class = GoodsinfoSerializer
#
#     #使用过滤器
#     filter_backends = (DjangoFilterBackend,)
#     #定义需要使用过滤器的字段
#     #filter_fields = ('name')
#     filter_class = Goodsinfofilter
