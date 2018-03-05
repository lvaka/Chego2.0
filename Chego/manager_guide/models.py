# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from manager_guide.choices import *

# Create your models here.
class MenuItem(models.Model):
	name = models.CharField(max_length=100)
	section = models.CharField(choices=section_choices,max_length=100)
	components = models.TextField()
	assembly = models.TextField()

	def __str__(self):
		return self.name

class Contact(models.Model):
	name = models.CharField(max_length=100)
	department = models.CharField(max_length=100)
	four11 = models.TextField()

	def __str__(self):
		return self.name

class Recipe(models.Model):
	name = models.CharField(max_length=100)
	ingredients = models.TextField()
	directions = models.TextField()

	def __str__(self):
		return self.name

class Purveyor(models.Model):
	name = models.CharField(choices=name_choices, max_length=100)
	email = models.CharField(max_length=100)
	contact = models.CharField(max_length=100)
	contact_number = models.CharField(max_length=12)

	def __str__(self):
		return self.name

class OrderList(models.Model):
	purveyor = models.CharField(choices=name_choices, max_length=100)
	item_name = models.CharField(max_length=100)
	unit = models.CharField(choices=unit_choices, max_length=20)
	pars = models.PositiveSmallIntegerField()
	

	def __str__(self):
		return self.item_name

class Order(models.Model):
	purveyor = models.CharField(choices=name_choices, max_length=100)
	item_name = models.CharField(max_length=100)
	quantity = models.PositiveSmallIntegerField()
	order_date = models.DateField(auto_now=True)
	ordernumber = models.PositiveIntegerField()
	delivery_date = models.CharField(choices=get_date_choices(7),max_length=100)


	def __str__(self):
		return self.purveyor