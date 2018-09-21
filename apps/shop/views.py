# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

#=========以下为前台页面-测试阶段就不分离了===============================
from django.shortcuts import render
def shop(request):
    """
    商品
    """
    return render(request,'shop/show.html')

