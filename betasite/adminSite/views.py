from django.shortcuts import render

from django.views.generic import TemplateView, ListView

from adminSite.models import Class, Donation, Donor, Events

class AdminHome(TemplateView):
	template_name = 'adminSite/home.html'


class DonorListView(ListView):
	template_name = 'adminSite/donorList.html'
	model = Donor

class EventListView(ListView):
	template_name = 'adminSite/eventList.html'
	model = Events

class DonationListView(ListView):
	template_name = 'adminSite/donationList.html'
	model = Donation

class ClassesListView(ListView):
	template_name = 'adminSite/classList.html'
	model = Class

class AddDonorView(TemplateView):
	template_name = 'adminSite/addDonor.html'

	def get_context_data(self, **kwargs):
		context = super(AddDonorView, self).get_context_data(**kwargs)
		context['classes'] = Class.objects.all()

		return context

class AddEventView(TemplateView):
	template_name = 'adminSite/addEvent.html'

class AddDonationView(TemplateView):
	template_name = 'adminSite/addDonation.html'

	def get_context_data(self, **kwargs):
		context = super(AddDonationView, self).get_context_data(**kwargs)
		context['donors'] = Donor.objects.all()
		context['events'] = Events.objects.all()

		return context