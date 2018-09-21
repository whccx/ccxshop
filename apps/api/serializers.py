# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from shop.models import Goodsinfo,Goodsparameter
from django.contrib.auth.models import User

# Serializers 定义API.
class GoodsinfoSerializer(serializers.ModelSerializer):

    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = Goodsinfo
        fields = "__all__"

#========================================================================
# Serializers 定义API.
class GoodsparameterSerializer(serializers.ModelSerializer):

    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = Goodsparameter
        fields = "__all__"

#===============================================================

class UserSerializer(serializers.ModelSerializer):
    Goodsinfo = serializers.PrimaryKeyRelatedField(many=True, queryset=Goodsinfo.objects.all())
    Goodsparameter = serializers.PrimaryKeyRelatedField(many=True, queryset=Goodsparameter.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'Goodsinfo','Goodsparameter')