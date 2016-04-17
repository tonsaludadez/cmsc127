
from django.conf.urls import url

from mainSite import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^about/$', views.AboutUs.as_view(), name='about'),
]
