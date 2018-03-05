# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from manager_guide.models import *

# Register your models here.
admin.site.register(MenuItem)
admin.site.register(Contact)
admin.site.register(Recipe)
admin.site.register(Purveyor)
admin.site.register(OrderList)
admin.site.register(Order)