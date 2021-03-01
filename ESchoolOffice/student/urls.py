from django.conf.urls import url
from .views import *


app_name = 'student'

urlpatterns = [
    url(r'^$', index, name='IndexForm'),
    # url(r'^$', StudentListView.as_view(), name='IndexForm'),
    url(r'^studentregistration/$', studentregistration, name='StudentRegistration'),

    ]
