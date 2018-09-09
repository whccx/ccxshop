# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from shop.models import Goods


from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from shop.serializers import ShopSerializer



# 开始.
@csrf_exempt
def goods_list(request):
    """
    商品列表.
    """
    if request.method == 'GET':
        show = Goods.objects.all()
        serializer = ShopSerializer(show, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ShopSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def goods_detail(request,pk):
    try:
        goods_one = Goods.objects.get(pk=pk)
    except Goods.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ShopSerializer(goods_one)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ShopSerializer(goods_one, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        goods_one.delete()
        return HttpResponse(status=204)


