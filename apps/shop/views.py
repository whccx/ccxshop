# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from shop import mixin #导入mixin.py文件
from shop.models import Goodsinfo,Goodsparameter
from shop.serializers import GoodsinfoSerializer,GoodsparameterSerializer
from rest_framework import generics
from rest_framework import permissions
from shop.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from shop.serializers import UserSerializer
from django.shortcuts import render

# 开始.
class GoodsinfoList(generics.ListCreateAPIView):
    """
    商品信息
    """
    queryset = Goodsinfo.objects.all()
    serializer_class = GoodsinfoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class GoodsinfoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    商品信息-操作
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                        IsOwnerOrReadOnly,)
    queryset = Goodsinfo.objects.all()
    serializer_class = GoodsinfoSerializer

#=======================================================================

# 开始.
class GoodsparameterList(generics.ListCreateAPIView):
    """
    商品参数
    """
    queryset = Goodsparameter.objects.all()
    serializer_class = GoodsparameterSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class GoodsparameterDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    商品参数-操作
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                        IsOwnerOrReadOnly,)
    queryset = Goodsparameter.objects.all()
    serializer_class = GoodsparameterSerializer


#====================================================================
def shop(request):
    """
    商品
    """
    return render(request,'shop/show.html')

@api_view(['GET'])
def shopin(request):
    """
    商品各类数据-url
    """
    if request.method == 'GET':
        show = {
            '商品信息':'http://127.0.0.1:8000/api/shop/goodsinfo',
            '商品参数': 'http://127.0.0.1:8000/api/shop/goodsparameter',
            '用户列表':'http://127.0.0.1:8000/api/shop/users',
        }
        return Response(show)
#====================================================================

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer