from django import forms
from manager_guide.models import *
from manager_guide.choices import *

class OrderCreationForm(forms.Form):

    def __init__(self, *args, **kwargs):
        item = kwargs.pop('item')
        super(OrderCreationForm, self).__init__(*args, **kwargs)

        for i, value in enumerate(item):

            self.fields['item_%s' % i] = forms.IntegerField(label=value, min_value=0, max_value=999, initial=0)


class DateForm(forms.Form):

	delivery_date = forms.ChoiceField(choices=get_date_choices(7))

class OrderForm(forms.ModelForm):

	class Meta:
		model = Order
		fields = ('delivery_date',)

class OrderFormItems(forms.Form):

	def __init__(self, *args, **kwargs):
		item = kwargs.pop('item')
		super(OrderFormItems, self).__init__(*args, **kwargs)

		for i, value in enumerate(item):
			labelstring = value.item_name + ' (' + value.unit + ')'

			self.fields['item_%s' % i] = forms.IntegerField(label=labelstring, min_value=0, max_value=999, initial=value.quantity)