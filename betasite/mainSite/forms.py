from django import forms

from django.contrib.auth import authenticate

class LoginForm(forms.Form):
	username = forms.CharField(max_length=20)
	password = forms.CharField(max_length=20)

	def clean(self):
		cleaned_data = super(LoginForm, self).clean()
		username = cleaned_data.get('username')
		password = cleaned_data.get('password')

		user = authenticate(username=username, password=password)

		if user:
			cleaned_data['user'] = user
		else:
			raise forms.ValidationError(
				'Username and/or password is incorrect.')
		
		return cleaned_data