from django.contrib.auth import login
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from mainSite.forms import LoginForm



# Create your views here.

class HomePage(TemplateView):
	template_name = 'mainSite/home.html'

	def get_context_data(self, *args, **kwargs):

		context = super(HomePage, self).get_context_data(*args, **kwargs)
		context['loginForm'] = LoginForm(data=self.request.POST)

		return context

	def post(self, request, *args, **kwargs):

		context = self.get_context_data(*args, **kwargs)
		form = context['loginForm']
		if form.is_valid():
			user = form.cleaned_data['user']
			login(request, user)
			return redirect('adminSite:adminHome')
		else:

			return


class AboutUs(TemplateView):
	template_name = 'mainSite/about.html'

	def get_context_data(self, *args, **kwargs):

		context = super(AboutUs, self).get_context_data(*args, **kwargs)
		context['loginForm'] = LoginForm(data=self.request.POST)

		return context

	def post(self, request, *args, **kwargs):

		context = self.get_context_data(*args, **kwargs)
		form = context['loginForm']
		if form.is_valid():
			user = form.cleaned_data['user']
			login(request, user)
			return redirect('adminSite:adminHome')
		else:

			return

