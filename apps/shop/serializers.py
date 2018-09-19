# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers, viewsets
from shop.models import Goodsinfo,Goodsparameter

# Serializers 定义API.
class GoodsinfoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = Goodsinfo
        fields = (
            'id',
            'goods_sn',
            'name',
            'market_price',
            'now_price',
            'goods_brief',
            'ship_free',
            'is_hot',
            'goods_brand',
            'goods_img'
        )

# ViewSets 定义view行为.
class GoodsinfoViewSet(viewsets.ModelViewSet):
    queryset = Goodsinfo.objects.all()
    serializer_class = GoodsinfoSerializer

#========================================================================
# Serializers 定义API.
class GoodsparameterSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = Goodsparameter
        fields = (
            'id',
            'goods_sn',
            'name',
            'goods_num',
            'goods_size',
            'goods_color'
        )

# ViewSets 定义view行为.
class GoodsparameterViewSet(viewsets.ModelViewSet):
    queryset = Goodsparameter.objects.all()
    serializer_class = GoodsparameterSerializer


#===============================================================

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    Goodsinfo = serializers.PrimaryKeyRelatedField(many=True, queryset=Goodsinfo.objects.all())
    Goodsparameter = serializers.PrimaryKeyRelatedField(many=True, queryset=Goodsparameter.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'Goodsinfo','Goodsparameter')