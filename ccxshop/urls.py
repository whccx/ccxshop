# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#网站ico
from django.views.generic.base import RedirectView

from django.urls import path,include
from django.contrib import admin

from . import views

urlpatterns = [
    #网站icon
    path('favicon.ico',RedirectView.as_view(url='static/favicon.ico')),

    path('admin/', admin.site.urls),
    path('', views.index),
    path('shop/', include('shop.urls',namespace='shop')),
]