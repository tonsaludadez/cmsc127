from django.conf.urls import url, include
from django.contrib import admin

from adminSite import views

urlpatterns = [
    url(r'^$', views.AdminHome.as_view(), name='adminHome'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^donors/$', views.DonorListView.as_view(), name='donorList'),
    url(r'^events/$', views.EventListView.as_view(), name='eventList'),
    url(r'^donations/$', views.DonationListView.as_view(), name='donationList'),
    url(r'^classes/$', views.ClassesListView.as_view(), name='classesList'),
    url(r'^donors/addDonor/$',views.AddDonorView.as_view(), name='addDonor'),
    url(r'^event/addEvent/$',views.AddEventView.as_view(), name='addEvent'),
    url(r'^donation/addDonation/$',views.AddDonationView.as_view(), name='addDonation'),
    url(r'^donor/submit/$',views.AddDonorForm, name='newDonor'),
    url(r'^class/submit/$',views.AddClassForm, name='newClass'),
    url(r'^donors/(?P<pk>[0-9]+)/$',views.DonorView.as_view(), name='donor'),
    url(r'^donors/delete/(?P<donorid>[0-9]+)/$',views.DeleteDonor, name='deleteDonor'),
    url(r'^donations/(?P<pk>[0-9]+)/$',views.DonationView.as_view(), name='donation'),
    url(r'^class/(?P<pk>[0-9]+)/$',views.ClassView.as_view(), name='class'),
    url(r'^class/modify/$',views.ModifyCoordinator, name='modifyCoor'),
]
