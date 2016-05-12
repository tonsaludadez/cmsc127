from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db.models import Sum
from django.shortcuts import redirect, render
from django.views.generic import  CreateView, DetailView, ListView, RedirectView, TemplateView

from adminSite.models import Class, Donation, Donor, Events, EventDonation, Transaction

import datetime

class LogoutView(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)

class AdminHome(LoginRequiredMixin, TemplateView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:adminHome'
	template_name = 'adminSite/home.html'

	def get_context_data(self, **kwargs):
		context = super(AdminHome, self).get_context_data(**kwargs)
		context['logs'] = LogEntry.objects.all()

		return context


class DonorListView(LoginRequiredMixin, ListView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:donorList'
	template_name = 'adminSite/donorList.html'
	model = Donor

class EventListView(LoginRequiredMixin, ListView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:eventList'
	template_name = 'adminSite/eventList.html'
	model = Events

class DonationListView(LoginRequiredMixin, ListView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:donationList'
	template_name = 'adminSite/donationList.html'
	model = Donation

class ClassesListView(LoginRequiredMixin, ListView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:classList'
	template_name = 'adminSite/classList.html'
	model = Class

class AddDonorView(LoginRequiredMixin, TemplateView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:addDonor'
	template_name = 'adminSite/addDonor.html'

	def get_context_data(self, **kwargs):
		context = super(AddDonorView, self).get_context_data(**kwargs)
		context['classes'] = Class.objects.all()
		context['donors'] = Donor.objects.all()

		return context

class EditDonorView(LoginRequiredMixin, TemplateView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:editDonor'
	template_name = 'adminSite/editDonor.html'

	def get_context_data(self, **kwargs):
		context = super(EditDonorView, self).get_context_data(**kwargs)
		donorid = self.kwargs['donorid']
		context['donor'] = Donor.objects.get(donorid=donorid)
		context['classes'] = Class.objects.all()
		context['donors'] = Donor.objects.all()

		return context

class AddEventView(LoginRequiredMixin, TemplateView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:addEvent'
	template_name = 'adminSite/addEvent.html'

class AddDonationView(LoginRequiredMixin, TemplateView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:addDonation'
	template_name = 'adminSite/addDonation.html'

	def get_context_data(self, **kwargs):
		context = super(AddDonationView, self).get_context_data(**kwargs)
		context['donors'] = Donor.objects.all()
		context['events'] = Events.objects.all()

		return context

class DonorView(LoginRequiredMixin, DetailView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:donorList'
	model = Donor
	context_object_name = 'donor'
	template_name = 'adminSite/donor.html'

	def get_context_data(self, **kwargs):
		context = super(DonorView, self).get_context_data(**kwargs)
		context['eventDonations'] = EventDonation.objects.filter(donorid=self.object.donorid)
		
		return context

class DonationView(LoginRequiredMixin, DetailView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:donationList'
	model = Donation
	context_object_name = 'donation'
	template_name = 'adminSite/donation.html'

	def get_context_data(self, **kwargs):
		context = super(DonationView, self).get_context_data(**kwargs)
		context['eventDonations'] = EventDonation.objects.filter(donationno=self.object.donationno)
		
		return context

class ClassView(LoginRequiredMixin, DetailView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:classList'
	model = Class
	context_object_name = 'class'
	template_name = 'adminSite/class.html'

class MonthlyReport(LoginRequiredMixin, TemplateView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:monthlyReport'
	template_name = 'adminSite/monthlyReportGenerator.html'

class AnnualReport(LoginRequiredMixin, TemplateView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:annualReport'
	template_name = 'adminSite/annualReportGenerator.html'

class EventView(LoginRequiredMixin, DetailView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:EventList'
	model = Events
	context_object_name = 'event'
	template_name = 'adminSite/event.html'

	def get_context_data(self, **kwargs):
		context = super(EventView, self).get_context_data(**kwargs)
		context['eventDonations'] = EventDonation.objects.filter(eventid=context['event'].eventid)
		return context

class EventReportGenerator(LoginRequiredMixin, TemplateView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:eventReportGenerator'
	template_name = 'adminSite/eventReportGenerator.html'

	def get_context_data(self, **kwargs):
		context = super(EventReportGenerator, self).get_context_data(**kwargs)
		context['events'] = Events.objects.all()

		return context

class EventReport(LoginRequiredMixin, DetailView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:eventReport'
	model = Events
	context_object_name = 'event'
	template_name = 'adminSite/eventReport.html'

def EventReportForm(request):
	eventid = Events.objects.get(eventid=request.POST['eventid'])
	return redirect('adminSite:EventReport', eventid)

def AddClassForm(request):
	classyear = request.POST['classyear']
	newClass = Class(classyear=classyear)
	
	newClass.save()
	
	LogEntry.objects.log_action(
		user_id=request.user.id,
		content_type_id=ContentType.objects.get_for_model(newClass).pk,
		object_id=newClass.classyear,
		object_repr=unicode(newClass),
		action_flag=ADDITION)

	return redirect('adminSite:classesList')

def AddDonorForm(request):
	fname = request.POST['fname']
	mname = request.POST['mname']
	lname = request.POST['lname']
	contactno = request.POST['contactno']
	creditno = request.POST['creditno']
	email = request.POST['email']
	class_field = Class.objects.get(classyear=request.POST['class_field'])
	newDonor = Donor(fname=fname, mname=mname, lname=lname, contactno=contactno, creditno=creditno, email=email, class_field=class_field)
	
	newDonor.save()
	
	LogEntry.objects.log_action(
		user_id=request.user.id,
		content_type_id=ContentType.objects.get_for_model(newDonor).pk,
		object_id=newDonor.donorid,
		object_repr=unicode(newDonor),
		action_flag=ADDITION)

	return redirect('adminSite:donorList')

def AddDonationForm(request):
	amount = request.POST['amount']
	pledge_date = request.POST['pledge_date']
	donorid = Donor.objects.get(donorid=request.POST['donorid'])
	newDonation = Donation(donorid=donorid, amount=amount,pledge_date=pledge_date)

	newDonation.save()

	LogEntry.objects.log_action(
		user_id=request.user.id,
		content_type_id=ContentType.objects.get_for_model(donationno).pk,
		object_id=newDonation.donationno,
		object_repr=unicode(newDonation),
		action_flag=ADDITION)

	if request.POST['eventid']:
		eventid = Events.objects.get(eventid=request.POST['eventid'])
		newEventDonation = EventDonation(donorid=donorid, donationno=newDonation, eventid=eventid)
		newEventDonation.save()

	return redirect('adminSite:donationList')

def AddEventForm(request):
	event_name = request.POST['event_name']
	event_date = request.POST['event_date']
	newEvent = Events(event_name=event_name, event_date=event_date)

	newEvent.save()

	LogEntry.objects.log_action(
		user_id=request.user.id,
		content_type_id=ContentType.objects.get_for_model(newEvent).pk,
		object_id=newEvent.eventid,
		object_repr=unicode(newEvent),
		action_flag=ADDITION)

	return redirect('adminSite:eventList')

def AddTransaction(request):
	donationno = Donation.objects.get(donationno=request.POST['donationno'])
	donorid = Donor.objects.get(donorid=request.POST['donorid'])
	amount_paid = request.POST['payment']
	date_paid = request.POST['date']
	newTransaction = Transaction(donationno=donationno, donorid=donorid, amount_paid=amount_paid, date_paid=date_paid)

	newTransaction.save()
	
	LogEntry.objects.log_action(
		user_id=request.user.id,
		content_type_id=ContentType.objects.get_for_model(newTransaction).pk,
		object_id=newTransaction.id,
		object_repr=unicode(newTransaction),
		action_flag=ADDITION)

	return redirect('adminSite:donationList')

def DeleteDonor(request, donorid):
	toDelete = Donor.objects.get(donorid=donorid)
	
	try:
		classYear = Class.objects.get(coordinator=donorid)
	except Exception, e:
		classYear = None

	if classYear:
		classYear.coordinator = None
		classYear.save()

	LogEntry.objects.log_action(
		user_id=request.user.id,
		content_type_id=ContentType.objects.get_for_model(toDelete).pk,
		object_id=toDelete.donorid,
		object_repr=unicode(toDelete),
		action_flag=DELETION)

	toDelete.delete()
	return redirect('adminSite:donorList')

def DeleteClass(request, classyear):
	toDelete = Class.objects.get(classyear=classyear)

	LogEntry.objects.log_action(
		user_id=request.user.id,
		content_type_id=ContentType.objects.get_for_model(toDelete).pk,
		object_id=toDelete.classyear,
		object_repr=unicode(toDelete.classyear),
		action_flag=DELETION)

	toDelete.delete()

	return redirect('adminSite:classesList')

def DeleteDonation(request, donationno):
	toDelete = Donation.objects.get(donationno=donationno)

	try:
		check = EventDonation.objects.get(donationno=toDelete)
	except Exception:
		check = None

	if check:
		deleteToo = EventDonation.objects.get(donationno=toDelete)
		deleteToo = EventDonation.objects.get(id=deleteToo.id)
		deleteToo.delete()

	Transaction.objects.filter(donationno=toDelete).delete()

	LogEntry.objects.log_action(
		user_id=request.user.id,
		content_type_id=ContentType.objects.get_for_model(toDelete).pk,
		object_id=toDelete.donationno,
		object_repr=unicode(toDelete.donationno),
		action_flag=DELETION)

	toDelete.delete()
	
	return redirect('adminSite:donationList')

def DeleteEvent(request, eventid):
	toDelete = Events.objects.get(eventid=eventid)

	try:
		check = EventDonation.objects.get(eventid=toDelete)
	except Exception:
		check = None

	if check:
		deleteToo = EventDonation.objects.get(eventid=eventid)
		deleteToo = EventDonation.objects.get(id=deleteToo.id)
		deleteToo.delete()

	LogEntry.objects.log_action(
		user_id=request.user.id,
		content_type_id=ContentType.objects.get_for_model(toDelete).pk,
		object_id=toDelete.eventid,
		object_repr=unicode(toDelete.event_name),
		action_flag=DELETION)

	toDelete.delete()

	return redirect('adminSite:eventList')

def ModifyCoordinator(request):
	newCoor = Donor.objects.get(donorid=request.POST['donor'])
	class_year = Class.objects.get(classyear=request.POST['class_year'])
	class_year.coordinator = newCoor

	LogEntry.objects.log_action(
		user_id=request.user.id,
		content_type_id=ContentType.objects.get_for_model(class_year).pk,
		object_id=class_year.classyear,
		object_repr=unicode(class_year),
		action_flag=CHANGE)

	class_year.save();

	return redirect('adminSite:classesList')

def ModifyDonor(request):
	donorid = request.POST['donorid']
	fname = request.POST['fname']
	mname = request.POST['mname']
	lname = request.POST['lname']
	contactno = request.POST['contactno']
	creditno = request.POST['creditno']
	email = request.POST['email']
	class_field = Class.objects.get(classyear=request.POST['class_field'])
	donor = Donor.objects.get(donorid=donorid)
	donor.fname = fname
	donor.mname = mname
	donor.lname = lname
	donor.contactno = contactno
	donor.creditno = creditno
	donor.email = email
	donor.class_field = class_field

	LogEntry.objects.log_action(
		user_id=request.user.id,
		content_type_id=ContentType.objects.get_for_model(donor).pk,
		object_id=donor.donorid,
		object_repr=unicode(donor),
		action_flag=CHANGE)

	donor.save()

	return redirect('adminSite:donorList')

