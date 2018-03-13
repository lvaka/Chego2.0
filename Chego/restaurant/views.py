# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from forms import CateringRequest
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context, Template
from django.template.loader import get_template
from django.http import JsonResponse


# Create your views here.
def restaurant(request):
	Cateringform = CateringRequest

	if request.method == 'POST':
		form = Cateringform(data=request.POST)

		if form.is_valid():
			client_name = request.POST.get('clientName', '')
			contact_email = request.POST.get('eMail', '')
			contact_phone = request.POST.get('phone', '')
			date = request.POST.get('date', '')
			notes = request.POST.get('notes', '')
                        
                        
			# Email the profile with the 
        	# catering information
			template = get_template('contact_template.txt')
			context = {
				'client_name': client_name,
				'contact_email': contact_email,
				'contact_phone': contact_phone,
				'date': date,
				'notes': notes,
				}

			content = template.render(context)
                        
			email = EmailMessage(
				"New Catering Request for " + date,
				content,
				'noreply@kogibbq.com',
				['eric@kogibbq.com', contact_email],
				headers = {'Reply-To': contact_email }
				)

			email.send()

			return redirect('main')

		else:
			return redirect('error')

	return render(request, 'restaurant.html', {'form': Cateringform})

def invalid_form(request):
	return render(request, 'oops.html')