from django import forms
from django.db import models
from manager_guide.choices import get_date_choices

class CateringRequest(forms.Form):
	clientName = forms.CharField(required=True, label='Name', max_length=100,
		widget=forms.TextInput(attrs ={'placeholder': 'Your name', 'size': '41'}))
	eMail = forms.EmailField(required=True, label='e-mail', max_length=100,
		widget=forms.TextInput(attrs={'placeholder': 'Contact Email', 'size': '41'}))
	phone = forms.CharField(required=True, label='phone', max_length=20,
		widget=forms.TextInput(attrs={'placeholder': 'Contact Number', 'size': '41'}))
	date = forms.ChoiceField(choices=get_date_choices(14), label='Date Requested', initial='', required=True, widget=forms.Select(attrs={'size': '1'}))
	notes = forms.CharField(required=True, label='Notes/Order' , max_length=100,
		widget=forms.Textarea(attrs={'placeholder': 'Please let us know how many guests you will be serving, which items you were interested in, and any allergies that you might want to inform us of.'}))