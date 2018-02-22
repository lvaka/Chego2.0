# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class MenuItem(models.Model):
	name = models.CharField(max_length=100)
	section = models.CharField(max_length=100)
	components = models.TextField()
	assembly = models.TextField()

	def publish(self):
		self.save

	def __str__(self):
		return self.name