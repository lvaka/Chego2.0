from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
	url(r'^$', views.restaurant, name='main'),
	url(r'^oops/$', views.invalid_form, name='error'),
]