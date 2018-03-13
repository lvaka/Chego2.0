from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
	url(r'^manager$', views.manager_guide, name='manager'),
	url(r'^manager/menu_items$', views.menu_items, name='menu_items'),
	url(r'^manager/contacts$', views.contacts, name='contacts'),
	url(r'^manager/recipes$', views.recipes, name='recipes'),
	url(r'^manager/order_selection$', views.order_selection, name='order_selection'),
	url(r'^manager/order/(?P<name>\w+)$', views.order, name='order'),
	url(r'^manager/order_history$', views.listorders, name='listorders'),
	url(r'^manager/editorder/(?P<pk>\d+)$', views.editorder, name='editorder'),
	url(r'^manager/confirmorder/(?P<pk>\d+)$', views.confirmorder, name='confirmorder'),
	url(r'^manager/removeorder/(?P<pk>\d+)$', views.deleteorder, name='deleteorder'),
]
