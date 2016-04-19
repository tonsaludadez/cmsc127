from django.conf.urls import url, include
from django.contrib import admin

from adminSite import views

urlpatterns = [
    url(r'^$', views.AdminHome.as_view(), name='adminHome'),
    url(r'^donors/$', views.DonorListView.as_view(), name='donorList'),
    url(r'^events/$', views.EventListView.as_view(), name='eventList'),
    url(r'^donations/$', views.DonationListView.as_view(), name='donationList'),
    url(r'^classes/$', views.ClassesListView.as_view(), name='classesList'),
    url(r'^donors/addDonor/$',views.AddDonorView.as_view(), name='addDonor'),
    url(r'^donors/addEvent/$',views.AddEventView.as_view(), name='addEvent'),
    url(r'^donors/addDonation/$',views.AddDonationView.as_view(), name='addDonation'),
]
