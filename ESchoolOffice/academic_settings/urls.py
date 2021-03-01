from django.urls import path
from . import views


urlpatterns = [
    #path('addsubject', views.SubjectAddForm.as_view(), name='add-subject'),
    path('subjects', views.SubjectListView.as_view(), name='subject-list'),
    #path('editsubject', views.SubjectEditForm.as_view(), name='edit-subject'),
    #path('addstandard', views.StandardAddForm.as_view(), name='add-standard'),
    path('standards', views.StandardListView.as_view(), name='standard-list'),
]