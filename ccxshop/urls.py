# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#网站ico
from django.views.generic.base import RedirectView

from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    #网站ico
    url(r'^favicon.ico$',RedirectView.as_view(url=r'static/favicon.ico')),

    url(r'^admin/', admin.site.urls),
    url(r'^shop/', include('shop.urls',namespace='shop')),
]