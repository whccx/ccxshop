# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

def index(request):
	return render(request,'index.html')

@api_view(['GET'])
def api(request):
	show = {
		'商品':'http://127.0.0.1:8000/api/shop',
	}
	return Response(show)