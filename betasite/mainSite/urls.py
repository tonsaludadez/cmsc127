
from django.conf.urls import url

from mainSite import views

urlpatterns = [
    url(r'^$',views.HomePage.as_view()),
]
