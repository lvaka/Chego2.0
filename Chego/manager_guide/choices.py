#Choices to be used for models and forms

from datetime import datetime, date, timedelta

name_choices = (
			('IFS', 'IFS'),
			('SYSCO', 'Sysco'),
			('PRODUCE', "Nature's Produce"),
			('MEAT', 'Rocker Bros'),
		)

section_choices = (
				('Snacks', 'Snacks'),
				('Grill', 'Grill'),
				('Wok', 'Wok'),
				('Sweets', 'Sweets'),
	)

unit_choices = (
			('#', 'lbs'),
			('cases', 'cases'),
			('bunches', 'bunches'),
			('each', 'each'),
			('tub', 'tub'),
			('bag', 'bag'),
			('quarts', 'quarts'),
			('gallon', 'gallon'),
			('bottle', 'bottle'),

	)

#Creating Date Choices

def get_date_choices(days):
	todays_date = datetime.today()
	date_choices = ()

	for i in range (days):
		todays_date += timedelta(days=1)
		date_tuple = (todays_date.strftime("%A %m/%d/%Y"), todays_date.strftime("%A %m/%d/%Y"),)
		date_choices += date_tuple,

	return date_choices