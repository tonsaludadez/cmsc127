from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.

class HomePage(TemplateView):
	template_name = 'mainSite/home.html'

class AboutUs(TemplateView):
	template_name = 'mainSite/about.html'
		

