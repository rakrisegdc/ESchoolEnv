from django.conf.urls import url
from .views import *
from .import views
from django.urls import path


app_name = 'student'

urlpatterns = [
    url(r'^$', views.StudentList.as_view(), name='IndexForm'),
    # url(r'^$', index, name='IndexForm'),
    url(r'^studentregistration/$', studentregistration, name='StudentRegistration'),
    path('studview/<int:pk>/', views.StudentView.as_view(), name='StudView'),

    ]
