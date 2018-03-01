# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import MenuItem, Contact, Recipe

# Register your models here.
admin.site.register(MenuItem)
admin.site.register(Contact)
admin.site.register(Recipe)