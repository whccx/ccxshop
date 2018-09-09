# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import path
from shop import views
app_name = 'shop'


urlpatterns = [
    path('show.html', views.show),
]