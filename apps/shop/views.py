# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from shop import mixin #导入mixin.py文件
from shop.models import Goods
from shop.serializers import ShopSerializer
from rest_framework import generics

# 开始.
class GoodsList(generics.ListCreateAPIView):
    queryset = Goods.objects.all()
    serializer_class = ShopSerializer

class GoodsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goods.objects.all()
    serializer_class = ShopSerializer


#====================================================================


from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def shopin(request):
    """
    商品页
    """
    if request.method == 'GET':
        show = {
            '女装':'http://127.0.0.1:8000/shop/goods',
            '男装': 'http://127.0.0.1:8000/shop/goods',
        }
        return Response(show)


