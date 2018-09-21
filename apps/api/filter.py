# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django_filters
from shop.models import Goodsinfo,Goodsparameter

class Goodsinfofilter(django_filters.rest_framework.FilterSet):
    """
    自定义过滤类
    """
    #price_min = django_filters.NumberFilter(name='market_price', lookup_expr='gte')
    #price_max = django_filters.NumberFilter(name='market_price', lookup_expr='lte')
    #name = django_filters.CharFilter(name='name', lookup_expr='icontains')
    class Meta:
        model = Goodsinfo
        fields = ['name','market_price','now_price']

class Goodsparameterfilter(django_filters.rest_framework.FilterSet):
    """
    自定义过滤类
    """
    class Meta:
        model = Goodsparameter
        fields = ['name']