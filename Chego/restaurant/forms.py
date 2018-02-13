from django import forms
from django.db import models

class CateringRequest(forms.Form):
	clientName = forms.CharField(required=True, label='Name', max_length=100,
		widget=forms.TextInput(attrs ={'placeholder': 'Your name', 'size': '41'}))
	eMail = forms.EmailField(required=True, label='e-mail', max_length=100,
		widget=forms.TextInput(attrs={'placeholder': 'Contact Email', 'size': '41'}))
	phone = forms.CharField(required=True, label='phone', max_length=20,
		widget=forms.TextInput(attrs={'placeholder': 'Contact Number', 'size': '41'}))
	date = forms.CharField(required=True, label='Date Requested', max_length=100,
		widget=forms.TextInput(attrs={'placeholder': 'Date you would like your event', 'size': '41'}))
	notes = forms.CharField(required=True, label='Notes/Order' , max_length=100,
		widget=forms.Textarea(attrs={'placeholder': 'Please let us know how many guests you will be serving, which items you were interested in, and any allergies that you might want to inform us of.'}))