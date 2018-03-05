# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from manager_guide.models import *

# Create your views here.

def manager_guide(request):

	return render(request, 'manager_guide/manager.html')

@login_required
def menu_items(request):

	snacks = MenuItem.objects.filter(section='Snacks').order_by('name')
	grills = MenuItem.objects.filter(section='Grill').order_by('name')
	woks = MenuItem.objects.filter(section='Wok').order_by('name')
	sweets = MenuItem.objects.filter(section='Sweets').order_by('name')


	return render(request, 'manager_guide/menu_items.html', {'snacks':snacks,
												'grills':grills,
												'woks':woks,
												'sweets':sweets})

@login_required
def contacts(request):

	contacts = Contact.objects.order_by('name')

	return render(request, 'manager_guide/contacts.html', {'contacts':contacts})

@login_required
def recipes(request):

	recipes = Recipe.objects.order_by('name')

	return render(request, 'manager_guide/recipes.html', {'recipes': recipes})

@login_required
def order_selection(request):

	purveyors = Purveyor.objects.order_by('name')

	return render(request, 'manager_guide/order_selection.html',
												{'purveyors': purveyors})