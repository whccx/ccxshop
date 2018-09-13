# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers, viewsets
from shop.models import Goods

# Serializers 定义API.
class ShopSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = Goods
        fields = (
            'id',
            'goods_sn',
            'name',
            'goods_num',
            'market_price',
            'now_price',
            'goods_brief',
            'ship_free',
            'is_hot',
            'add_time'
        )

# ViewSets 定义view行为.
class ShopViewSet(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = ShopSerializer


from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    shop = serializers.PrimaryKeyRelatedField(many=True, queryset=Goods.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'shop')