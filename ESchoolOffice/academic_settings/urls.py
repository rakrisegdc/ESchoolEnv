from django.urls import path
from . import views


urlpatterns = [
    path('addsubject', views.addsubject, name='addsubject'),
    path('subjects', views.indexsubjects, name='indexsubject'),
    path('addstandard', views.addstandard, name='addstandard'),
    path('subject', views.IndexView.as_view(), name='addstandard'),
]