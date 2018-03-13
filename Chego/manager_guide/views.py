# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from manager_guide.models import *
from manager_guide.forms import *

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

@login_required
def order(request, name):

	orders = OrderList.objects.filter(purveyor=name)

	if request.method == 'POST':
		form = OrderCreationForm(item=orders, data=request.POST)

		print(form.data)

		if form.is_valid():
			deliverydate = form.data['delivery_date']


			neworder = Order(purveyor=name, delivery_date=deliverydate)
			neworder.save()

			for i, item in enumerate(orders):

				orderentry = OrderedItem(order=neworder, 
										item_name=item.item_name, 
										unit=item.unit, 
										quantity=form.data['item_%s' % i]
										)
				orderentry.save()



			return redirect('confirmorder', pk=neworder.pk)

	else:
		form = OrderCreationForm(item=orders)
		dateform = DateForm


		return render (request, 'manager_guide/order.html', 
									{'orders': orders, 
									'purveyor': name, 
									'form': form,
									'dateform': dateform})

@login_required
def editorder(request, pk):

	order = get_object_or_404(Order, pk=pk)
	ordereditems = OrderedItem.objects.filter(order=pk) 

	form = OrderForm(instance=order)
	formitems = OrderFormItems(item=ordereditems)

	if request.method == 'POST':
		form = OrderForm(instance=order, data=request.POST)
		formitems = OrderFormItems(item=ordereditems, data=request.POST)

		if(form.is_valid() and formitems.is_valid()):
			form.save()
			for i, item in enumerate(formitems):
				if (int(item.data) != ordereditems[i].quantity):
					OrderedItem.objects.filter(id=ordereditems[i].pk).update(quantity=item.data)
				

		return redirect('confirmorder', pk=pk)




	return render (request, 'manager_guide/editorder.html', 
							{'form': form,
							'formitems': formitems, 
							'order': order})

@login_required
def confirmorder(request, pk):
	order = get_object_or_404(Order, pk=pk)
	ordereditems = OrderedItem.objects.filter(order=pk, quantity__gt = 0)

	return render(request, 'manager_guide/confirmorder.html',
							{'order':order,
							'ordereditems':ordereditems})

@login_required
def deleteorder(request, pk):

	order = get_object_or_404(Order, pk=pk)
	order.delete()
	return redirect('order_selection')

@login_required
def listorders(request):

	orders = Order.objects.all()

	return render(request, 'manager_guide/listorders.html', {'orders': orders})

@login_required
def submitorder(request, pk):

	order = get_object_or_404(Order, pk=pk)
	ordereditems = ordereditems = OrderedItem.objects.filter(order=pk, quantity__gt = 0)

	#Simply Activates Bool that E-Mail has been sent.  No actual logic
	order.SendEmail()

	return redirect('listorders')