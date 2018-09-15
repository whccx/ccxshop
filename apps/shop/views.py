# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from shop import mixin #导入mixin.py文件
from shop.models import Goods
from shop.serializers import ShopSerializer
from rest_framework import generics
from rest_framework import permissions
from shop.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from shop.serializers import UserSerializer
from django.shortcuts import render

# 开始.
class GoodsList(generics.ListCreateAPIView):
    queryset = Goods.objects.all()
    serializer_class = ShopSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class GoodsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                        IsOwnerOrReadOnly,)
    queryset = Goods.objects.all()
    serializer_class = ShopSerializer

#====================================================================
def shop(request):
    return render(request,'shop/show.html')

@api_view(['GET'])
def shopin(request):
    """
    商品页
    """
    if request.method == 'GET':
        show = {
            '女装':'http://127.0.0.1:8000/api/shop/goods',
            '男装':'http://127.0.0.1:8000/api/shop/goods',
        }
        return Response(show)
#====================================================================

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer