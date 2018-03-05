from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
	url(r'^manager$', views.manager_guide, name='manager'),
	url(r'^menu_items$', views.menu_items, name='menu_items'),
	url(r'^contacts$', views.contacts, name='contacts'),
	url(r'^recipes$', views.recipes, name='recipes'),
	url(r'^order_selection$', views.order_selection, name='order_selection'),
]
