from django.urls import path
from . import views


urlpatterns = [
    path('addsubject', views.addsubject, name='addsubject'),
    path('subjects', views.indexsubjects, name='indexsubject'),
]