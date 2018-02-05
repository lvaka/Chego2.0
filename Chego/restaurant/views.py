# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def restaurant(request):
	return render(request, 'restaurant.html')