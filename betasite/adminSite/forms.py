from django import forms

from adminSite.models import Donor

class DonorForm(forms.ModelForm):
	model = Donor
	fields = ['fname', 'mname', 'lname','class_year', 'contact-no', 'email', 'credit-card-no']