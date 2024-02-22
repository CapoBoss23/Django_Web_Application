import datetime
from django import forms
from django.core.exceptions import ValidationError


# form used to insert data about translation by athenticated users
class TranslatedTextForm(forms.Form):
	# form fields
	new_translated_title = forms.CharField(max_length=100)
	new_translated_content = forms.CharField(widget=forms.Textarea, max_length=2000)
	
	# validation methods, one for each form field. no check is applied here as
	# max_lenght and blank constraints are automatically checked in each field

	def clean_new_translated_title(self):
		data = self.cleaned_data['new_translated_title']
		return data

	def clean_new_translated_content(self):
		data = self.cleaned_data['new_translated_content']
		return data