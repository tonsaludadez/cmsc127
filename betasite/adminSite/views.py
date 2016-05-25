from django.contrib.auth.decorators import login_required
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group
from django.contrib.contenttypes.models import ContentType
from django.db.models import Sum
from django.shortcuts import redirect, render
from django.views.generic import  CreateView, DetailView, ListView, RedirectView, TemplateView
from django.views.generic.dates import YearArchiveView, MonthArchiveView

from adminSite.models import Class, Donation, Donor, Events, EventDonation, Transaction

import datetime

from itertools import chain

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
		context['is_admin'] = not self.request.user.groups.all().exists()

		return context


class DonorListView(LoginRequiredMixin, ListView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:donorList'
	template_name = 'adminSite/donorList.html'
	model = Donor

	def get_context_data(self, **kwargs):
		context = super(DonorListView, self).get_context_data(**kwargs)
		context['is_not_authorized'] = self.request.user.groups.filter(name='Coordinator').exists()
		context['is_admin'] = not self.request.user.groups.all().exists()

		return context

class PotentialDonorsView(LoginRequiredMixin, ListView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:potentialDonors'
	template_name = 'adminSite/potentialDonors.html'
	model = Donor

	def get_context_data(self, **kwargs):
		context = super(PotentialDonorsView, self).get_context_data(**kwargs)
		context['is_not_authorized'] = self.request.user.groups.filter(name='Coordinator').exists()
		context['is_admin'] = not self.request.user.groups.all().exists()

		return context

class EventListView(LoginRequiredMixin, ListView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:eventList'
	template_name = 'adminSite/eventList.html'
	model = Events

	def get_context_data(self, **kwargs):
		context = super(EventListView, self).get_context_data(**kwargs)
		context['is_not_authorized'] = self.request.user.groups.filter(name='Coordinator').exists()
		context['is_admin'] = not self.request.user.groups.all().exists()

		return context

class DonationListView(LoginRequiredMixin, ListView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:donationList'
	template_name = 'adminSite/donationList.html'
	model = Donation

	def get_context_data(self, **kwargs):
		context = super(DonationListView, self).get_context_data(**kwargs)
		context['is_not_authorized'] = self.request.user.groups.filter(name='Coordinator').exists()
		context['is_admin'] = not self.request.user.groups.all().exists()

		return context

class ClassesListView(LoginRequiredMixin, ListView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:classList'
	template_name = 'adminSite/classList.html'
	model = Class

	def get_context_data(self, **kwargs):
		context = super(ClassesListView, self).get_context_data(**kwargs)
		context['is_not_authorized'] = self.request.user.groups.filter(name='Coordinator').exists()
		context['is_admin'] = not self.request.user.groups.all().exists()

		return context

class UserListView(LoginRequiredMixin, ListView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:userList'
	template_name = 'adminSite/userList.html'
	model = User

	def get_context_data(self, **kwargs):
		context = super(UserListView, self).get_context_data(**kwargs)
		context['is_not_authorized'] = self.request.user.groups.filter(name='Coordinator').exists()
		context['is_admin'] = not self.request.user.groups.all().exists()

		return context

	def get(self, request, *args, **kwargs):
		if request.user.groups.all().exists():
			return redirect('adminSite:adminHome')
		return super(UserListView, self).get(request, *args, **kwargs)

class AddDonorView(LoginRequiredMixin, TemplateView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:addDonor'
	template_name = 'adminSite/addDonor.html'

	def get_context_data(self, **kwargs):
		context = super(AddDonorView, self).get_context_data(**kwargs)
		context['classes'] = Class.objects.all()
		context['donors'] = Donor.objects.all()
		context['is_admin'] = not self.request.user.groups.all().exists()

		return context

	def get(self, request, *args, **kwargs):
		if request.user.groups.filter(name='Coordinator').exists():
			return redirect('adminSite:adminHome')
		return super(AddDonorView, self).get(request, *args, **kwargs)

class AddUserView(LoginRequiredMixin, TemplateView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:addUser'
	template_name = 'adminSite/addUser.html'

	def get_context_data(self, **kwargs):
		context = super(AddUserView, self).get_context_data(**kwargs)
		context['is_admin'] = not self.request.user.groups.all().exists()
		context['groups'] = Group.objects.all()

		return context

	def get(self, request, *args, **kwargs):
		if request.user.groups.all().exists():
			return redirect('adminSite:adminHome')
		return super(AddUserView, self).get(request, *args, **kwargs)

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
		context['is_admin'] = not self.request.user.groups.all().exists()

		return context

	def get(self, request, *args, **kwargs):
		if request.user.groups.filter(name='Coordinator').exists():
			return redirect('adminSite:adminHome')
		return super(EditDonorView, self).get(request, *args, **kwargs)

class AddEventView(LoginRequiredMixin, TemplateView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:addEvent'
	template_name = 'adminSite/addEvent.html'

	def get_context_data(self, **kwargs):
		context = super(AddEventView, self).get_context_data(**kwargs)
		context['is_admin'] = not self.request.user.groups.all().exists()

		return context

	def get(self, request, *args, **kwargs):
		if request.user.groups.filter(name='Coordinator').exists():
			return redirect('adminSite:adminHome')
		return super(AddEventView, self).get(request, *args, **kwargs)

class AddDonationView(LoginRequiredMixin, TemplateView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:addDonation'
	template_name = 'adminSite/addDonation.html'

	def get_context_data(self, **kwargs):
		context = super(AddDonationView, self).get_context_data(**kwargs)
		context['donors'] = Donor.objects.all()
		context['events'] = Events.objects.all()
		context['is_admin'] = not self.request.user.groups.all().exists()

		return context

	def get(self, request, *args, **kwargs):
		if request.user.groups.filter(name='Coordinator').exists():
			return redirect('adminSite:adminHome')
		return super(AddDonationView, self).get(request, *args, **kwargs)

class DonorView(LoginRequiredMixin, DetailView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:donorList'
	model = Donor
	context_object_name = 'donor'
	template_name = 'adminSite/donor.html'

	def get_context_data(self, **kwargs):
		context = super(DonorView, self).get_context_data(**kwargs)
		context['eventDonations'] = EventDonation.objects.filter(donorid=self.object.donorid)
		context['is_not_authorized'] = self.request.user.groups.filter(name='Coordinator').exists()
		context['is_admin'] = not self.request.user.groups.all().exists()
		
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
		context['is_not_authorized'] = self.request.user.groups.filter(name='Coordinator').exists()
		context['is_admin'] = not self.request.user.groups.all().exists()

		return context

class ClassView(LoginRequiredMixin, DetailView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:classList'
	model = Class
	context_object_name = 'class'
	template_name = 'adminSite/class.html'

	def get_context_data(self, **kwargs):
		context = super(ClassView, self).get_context_data(**kwargs)
		context['is_not_authorized'] = self.request.user.groups.filter(name='Coordinator').exists()
		context['is_admin'] = not self.request.user.groups.all().exists()
		
		return context

class UserView(LoginRequiredMixin, TemplateView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:userList'
	template_name = 'adminSite/user.html'

	def get_context_data(self, **kwargs):
		context = super(UserView, self).get_context_data(**kwargs)
		pk = self.kwargs['pk']
		context['is_not_authorized'] = self.request.user.groups.filter(name='Coordinator').exists()
		context['is_admin'] = not self.request.user.groups.all().exists()
		context['user'] = User.objects.get(pk=pk)
		context['groups'] = Group.objects.all()
		
		return context

	def get(self, request, *args, **kwargs):
		if request.user.groups.all().exists():
			return redirect('adminSite:adminHome')
		return super(UserView, self).get(request, *args, **kwargs)

class DuePaymentsGenerator(LoginRequiredMixin, TemplateView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:duePaymentsGenerator'
	template_name = 'adminSite/duePaymentsGenerator.html'

	def get_context_data(self, **kwargs):
		context = super(DuePaymentsGenerator, self).get_context_data(**kwargs)
		context['is_admin'] = not self.request.user.groups.all().exists()
		
		return context

class DuePayments(LoginRequiredMixin, MonthArchiveView):
	queryset = Transaction.objects.all()
	date_field = "date_paid"
	allow_future = False
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:duePayments'
	template_name = 'adminSite/duePayments.html'

	def get_context_data(self, **kwargs):
		context = super(DuePayments, self).get_context_data(**kwargs)

		donors = {}
		pledges = {}

		for transaction in context['object_list']:
			if not transaction.donationno in donors:
				donors[transaction.donationno] = transaction.amount_paid
			else:
				donors[transaction.donationno] = donors[transaction.donationno] + transaction.amount_paid

		for transaction in context['object_list']:
			pledges[transaction.donationno] = transaction.donationno.amount

		context['donors'] = donors
		context['pledges'] = pledges
		context['is_admin'] = not self.request.user.groups.all().exists()

		return context

class MonthlyReportGenerator(LoginRequiredMixin, TemplateView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:monthlyReportGenerator'
	template_name = 'adminSite/monthlyReportGenerator.html'

	def get_context_data(self, **kwargs):
		context = super(MonthlyReportGenerator, self).get_context_data(**kwargs)
		context['is_admin'] = not self.request.user.groups.all().exists()
		
		return context

class MonthlyReport(LoginRequiredMixin, MonthArchiveView):
	queryset = Transaction.objects.all()
	date_field = "date_paid"
	allow_future = False
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:monthlyReport'
	template_name = 'adminSite/monthlyReport.html'

	def get_context_data(self, **kwargs):
		context = super(MonthlyReport, self).get_context_data(**kwargs)
		sum_paid = 0
		sum_pledge = 0
		for transaction in context['object_list']:
			sum_paid = sum_paid + transaction.amount_paid
			sum_pledge = sum_pledge + transaction.donationno.amount

		context['sum_paid'] = sum_paid
		context['sum_pledge'] = sum_pledge
		context['is_admin'] = not self.request.user.groups.all().exists()

		return context

class AnnualReportGenerator(LoginRequiredMixin, TemplateView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:annualReportGenerator'
	template_name = 'adminSite/annualReportGenerator.html'

	def get_context_data(self, **kwargs):
		context = super(AnnualReportGenerator, self).get_context_data(**kwargs)
		context['is_admin'] = not self.request.user.groups.all().exists()
		
		return context

class AnnualReport(LoginRequiredMixin, YearArchiveView):
	login_url = 'mainSite:home'
	queryset = Transaction.objects.all()
	date_field = "date_paid"
	make_object_list = True
	allow_future = False
	template_name = 'adminSite/annualReport.html'

	def get_context_data(self, **kwargs):
		context = super(AnnualReport, self).get_context_data(**kwargs)
		
		classes = {}

		for transaction in context['object_list']:
			if not transaction.donorid.class_field in classes:
				classes[transaction.donorid.class_field] = transaction.amount_paid
			else:
				classes[transaction.donorid.class_field] = classes[transaction.donorid.class_field] + transaction.amount_paid

		context['classes'] = classes
		context['is_admin'] = not self.request.user.groups.all().exists()
		context['donors'] = Donor.objects.all()

		return context

class EventView(LoginRequiredMixin, DetailView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:EventList'
	model = Events
	context_object_name = 'event'
	template_name = 'adminSite/event.html'

	def get_context_data(self, **kwargs):
		context = super(EventView, self).get_context_data(**kwargs)
		context['eventDonations'] = EventDonation.objects.filter(eventid=context['event'].eventid)
		context['is_admin'] = not self.request.user.groups.all().exists()

		return context

class CoordinatorListGenerator(LoginRequiredMixin, TemplateView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:coordinatorListGenerator'
	template_name = 'adminSite/coordinatorListGenerator.html'

	def get_context_data(self, **kwargs):
		context = super(CoordinatorListGenerator, self).get_context_data(**kwargs)
		context['classes'] = Class.objects.all()
		context['is_admin'] = not self.request.user.groups.all().exists()

		return context

class CoordinatorList(LoginRequiredMixin, DetailView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:coordinatorList'
	template_name = 'adminSite/coordinatorList.html'
	model = Class
	context_object_name = 'class'

	def get_context_data(self, **kwargs):
		context = super(CoordinatorList, self).get_context_data(**kwargs)
		context['is_not_authorized'] = self.request.user.groups.filter(name='Coordinator').exists()
		context['is_admin'] = not self.request.user.groups.all().exists()
		lastyear = {}
		thisyear = {}

		for donor in context['class'].donors.all():
			lastyear[donor] = donor.donations.filter(pledge_date__year=2015)

		context['last_year'] = lastyear

		for donor in context['class'].donors.all():
			thisyear[donor] = donor.donations.filter(pledge_date__year=2016)

		context['this_year'] = thisyear

		print context['this_year']
		return context

class EventReportGenerator(LoginRequiredMixin, TemplateView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:eventReportGenerator'
	template_name = 'adminSite/eventReportGenerator.html'

	def get_context_data(self, **kwargs):
		context = super(EventReportGenerator, self).get_context_data(**kwargs)
		context['events'] = Events.objects.all()
		context['is_admin'] = not self.request.user.groups.all().exists()

		return context

class EventReport(LoginRequiredMixin, DetailView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:eventReport'
	model = Events
	context_object_name = 'event'
	template_name = 'adminSite/eventReport.html'

	def get_context_data(self, **kwargs):
		context = super(EventReport, self).get_context_data(**kwargs)
		context['eventDonations'] = EventDonation.objects.filter(eventid=kwargs['object'])
		context['is_admin'] = not self.request.user.groups.all().exists()

		return context

class SearchDonor(LoginRequiredMixin, ListView):
	login_url = 'mainSite:home'
	redirect_field_name = 'adminSite:userList'
	template_name = 'adminSite/searchDonorList.html'
	model = Donor

	def get_queryset(self):
		queryset = super(SearchDonor, self).get_queryset()
		names = self.request.GET['search']
		names = names.split(' ')
		toReturn = 0
		toReturn = []
		for name in names:
			fname = queryset.filter(fname__icontains=name)
			lname = queryset.filter(lname__icontains=name)
			toReturn = list(chain(fname, lname))
		return toReturn

	def get_context_data(self, **kwargs):
		context = super(SearchDonor, self).get_context_data(**kwargs)
		context['searched'] = self.request.GET['search']

		return context

@login_required(login_url='mainSite:home')
def EventReportForm(request):
	event = Events.objects.get(eventid=request.POST['eventid'])
	print event
	return redirect('adminSite:eventReport', event)

@login_required(redirect_field_name='my_redirect_field')
def AddClassForm(request):
	if request.user.groups.filter(name='Coordinator').exists():
		return redirect('adminSite:adminHome')
		
	classyear = request.POST['classyear']
	newClass = Class(classyear=classyear)
	
	try:
		if request.user.groups.filter(name='Coordinator').exists():
			newClass.save(using='coordinator')
		else :
			newClass.save()
	except Exception, e:
		return redirect('adminSite:classesList')
		
	LogEntry.objects.log_action(
		user_id=request.user.id,
		content_type_id=ContentType.objects.get_for_model(newClass).pk,
		object_id=newClass.classyear,
		object_repr=unicode(newClass),
		action_flag=ADDITION)

	return redirect('adminSite:classesList')

@login_required(login_url='mainSite:home')
def AddDonorForm(request):
	if request.user.groups.filter(name='Coordinator').exists():
		return redirect('adminSite:adminHome')

	fname = request.POST['fname']
	mname = request.POST['mname']
	lname = request.POST['lname']
	contactno = request.POST['contactno']
	creditno = request.POST['creditno']
	email = request.POST['email']
	address = request.POST['address']
	class_field = Class.objects.get(classyear=request.POST['class_field'])
	if request.POST['affiliation']:
		affiliation = request.POST['affiliation']
		affiliation = Donor.objects.get(donorid=affiliation)
		newDonor = Donor(fname=fname, mname=mname, lname=lname, contactno=contactno, creditno=creditno, email=email, class_field=class_field, address=address, donor_affiliation=affiliation)
	else:
		newDonor = Donor(fname=fname, mname=mname, lname=lname, contactno=contactno, creditno=creditno, email=email, class_field=class_field, address=address)
	
	try:
		if request.user.groups.filter(name='Coordinator').exists():
			newDonor.save(using='coordinator')
		else :
			newDonor.save()
	except Exception, e:
		return redirect('adminSite:donorList')

	LogEntry.objects.log_action(
		user_id=request.user.id,
		content_type_id=ContentType.objects.get_for_model(newDonor).pk,
		object_id=newDonor.donorid,
		object_repr=unicode(newDonor),
		action_flag=ADDITION)

	return redirect('adminSite:donorList')

@login_required(login_url='mainSite:home')
def AddUserForm(request):
	if request.user.groups.all().exists():
		return redirect('adminSite:adminHome')

	username = request.POST['username']
	password = request.POST['password']
	last_name = request.POST['last_name']
	first_name = request.POST['first_name']
	email = request.POST['email']
	groups = Group.objects.get(name=request.POST['groups'])
	newUser = User(username=username, last_name=last_name, first_name=first_name,email=email)
	newUser.set_password(password)
	newUser.save()

	groups.user_set.add(newUser)

	LogEntry.objects.log_action(
		user_id=request.user.id,
		content_type_id=ContentType.objects.get_for_model(newUser).pk,
		object_id=newUser.pk,
		object_repr=unicode(newUser),
		action_flag=ADDITION)

	return redirect('adminSite:userList')

@login_required(login_url='mainSite:home')
def AddDonationForm(request):
	if request.user.groups.filter(name='Coordinator').exists():
		return redirect('adminSite:adminHome')

	amount = request.POST['amount']
	pledge_date = request.POST['pledge_date']
	donorid = Donor.objects.get(donorid=request.POST['donorid'])
	newDonation = Donation(donorid=donorid, amount=amount,pledge_date=pledge_date)
	
	try:
		if request.user.groups.filter(name='Coordinator').exists():
			newDonation.save(using='coordinator')
		else :
			newDonation.save()
	except Exception, e:
		return redirect('adminSite:donationList')

	LogEntry.objects.log_action(
		user_id=request.user.id,
		content_type_id=ContentType.objects.get_for_model(newDonation).pk,
		object_id=newDonation.donationno,
		object_repr=unicode(newDonation),
		action_flag=ADDITION)

	if request.POST['eventid']:
		eventid = Events.objects.get(eventid=request.POST['eventid'])
		newEventDonation = EventDonation(donorid=donorid, donationno=newDonation, eventid=eventid)
		newEventDonation.save()

	return redirect('adminSite:donationList')

@login_required(login_url='mainSite:home')
def AddEventForm(request):
	if request.user.groups.filter(name='Coordinator').exists():
		return redirect('adminSite:adminHome')

	event_name = request.POST['event_name']
	event_date = request.POST['event_date']
	newEvent = Events(event_name=event_name, event_date=event_date)

	try:
		if request.user.groups.filter(name='Coordinator').exists():
			newEvent.save(using='coordinator')
		else :
			newEvent.save()
	except Exception, e:
		print "Error"
		return redirect('adminSite:eventList')

	LogEntry.objects.log_action(
		user_id=request.user.id,
		content_type_id=ContentType.objects.get_for_model(newEvent).pk,
		object_id=newEvent.eventid,
		object_repr=unicode(newEvent),
		action_flag=ADDITION)

	return redirect('adminSite:eventList')

@login_required(login_url='mainSite:home')
def AddTransaction(request):
	if request.user.groups.filter(name='Coordinator').exists():
		return redirect('adminSite:adminHome')

	donationno = Donation.objects.get(donationno=request.POST['donationno'])
	donorid = Donor.objects.get(donorid=request.POST['donorid'])
	amount_paid = request.POST['payment']
	date_paid = request.POST['date']
	newTransaction = Transaction(donationno=donationno, donorid=donorid, amount_paid=amount_paid, date_paid=date_paid)

	try:
		if request.user.groups.filter(name='Coordinator').exists():
			newTransaction.save(using='coordinator')
		else :
			newTransaction.save()
	except Exception, e:
		return redirect('adminSite:donationList')
	
	LogEntry.objects.log_action(
		user_id=request.user.id,
		content_type_id=ContentType.objects.get_for_model(newTransaction).pk,
		object_id=newTransaction,
		object_repr=unicode(newTransaction),
		change_message='Added New Payment',
		action_flag=ADDITION)

	return redirect('adminSite:donationList')

@login_required(login_url='mainSite:home')
def DeleteDonor(request, donorid):
	if request.user.groups.filter(name='Coordinator').exists():
		return redirect('adminSite:donorList')

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

@login_required(login_url='mainSite:home')
def DeleteClass(request, classyear):
	if request.user.groups.filter(name='Coordinator').exists():
		return redirect('adminSite:classesList')
	
	toDelete = Class.objects.get(classyear=classyear)

	LogEntry.objects.log_action(
		user_id=request.user.id,
		content_type_id=ContentType.objects.get_for_model(toDelete).pk,
		object_id=toDelete.classyear,
		object_repr=unicode(toDelete.classyear),
		action_flag=DELETION)

	toDelete.delete()

	return redirect('adminSite:classesList')

@login_required(login_url='mainSite:home')
def DeleteDonation(request, donationno):
	if request.user.groups.filter(name='Coordinator').exists():
		return redirect('adminSite:donationList')

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

@login_required(login_url='mainSite:home')
def DeleteEvent(request, eventid):
	if request.user.groups.filter(name='Coordinator').exists():
		return redirect('adminSite:eventList')

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

@login_required(login_url='mainSite:home')
def DeleteUser(request, pk):
	if request.user.groups.all().exists():
		return redirect('adminSite:adminHome')

	toDelete = User.objects.get(pk=pk)

	LogEntry.objects.log_action(
		user_id=request.user.id,
		content_type_id=ContentType.objects.get_for_model(toDelete).pk,
		object_id=toDelete.pk,
		object_repr=unicode(toDelete.username),
		action_flag=DELETION)

	toDelete.delete()
	
	return redirect('adminSite:userList')

@login_required(login_url='mainSite:home')
def ModifyCoordinator(request):
	if request.user.groups.filter(name='Coordinator').exists():
		return redirect('adminSite:classesList')

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

@login_required(login_url='mainSite:home')
def ModifyUser(request):
	if request.user.groups.all().exists():
		return redirect('adminSite:adminHome')

	pk = request.POST['pk']
	last_name = request.POST['last_name']
	first_name = request.POST['first_name']
	email = request.POST['email']
	groups = Group.objects.get(name=request.POST['groups'])
	user = User.objects.get(pk=pk)
	old_group = user.groups.all()[0]
	user.last_name = last_name
	user.first_name = first_name
	user.email = email
	user.save()

	old_group.user_set.remove(user)
	groups.user_set.add(user)

	LogEntry.objects.log_action(
		user_id=request.user.id,
		content_type_id=ContentType.objects.get_for_model(user).pk,
		object_id=user.pk,
		object_repr=unicode(user),
		action_flag=CHANGE)

	return redirect('adminSite:userList')

@login_required(login_url='mainSite:home')
def ModifyDonor(request):
	if request.user.groups.filter(name='Coordinator').exists():
		return redirect('adminSite:donorList')

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

	if request.POST['affiliation']:
		affiliation = request.POST['affiliation']
		affiliation = Donor.objects.get(donorid=affiliation)

		donor.donor_affiliation = affiliation
	

	LogEntry.objects.log_action(
		user_id=request.user.id,
		content_type_id=ContentType.objects.get_for_model(donor).pk,
		object_id=donor.donorid,
		object_repr=unicode(donor),
		action_flag=CHANGE)

	donor.save()

	return redirect('adminSite:donorList')

@login_required(login_url='mainSite:home')
def redirectMonthlyReport(request):
	return redirect('adminSite:monthlyReport', request.POST['year'], request.POST['month'])

@login_required(login_url='mainSite:home')
def redirectToAnnualYear(request):
	return redirect('adminSite:annualReport', request.POST['year'])

@login_required(login_url='mainSite:home')
def redirectDuePayments(request):
	return redirect('adminSite:duePayments', request.POST['year'], request.POST['month'])

@login_required(login_url='mainSite:home')
def redirectCoordinatorList(request):
	return redirect('adminSite:coordinatorList', request.POST['class_field'])
