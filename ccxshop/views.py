# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def index(request):
	show = {'商品':'http://127.0.0.1:8000/shop',}
	return Response(show)