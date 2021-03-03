from django.urls import path
from . import views


urlpatterns = [
    path('subjects', views.SubjectListView.as_view(), name='subject-list'),
    path('addsubject', views.SubjectAddForm.as_view(), name='add-subject'),
    #path('editsubject/<int:id>/', views.subject_edit, name='edit-subject'),
    path('deletesubject/<int:id>/', views.delete_subject, name='delete-subject'),

    path('standards', views.StandardListView.as_view(), name='standard-list'),
    path('addstandard', views.StandardAddForm.as_view(), name='add-standard'),
    path('deletestandard/<int:id>/', views.delete_standard, name='delete-standard'),

    path('divisions', views.DivisionListView.as_view(), name='division-list'),
    path('adddivision', views.DivisionAddForm.as_view(), name='add-division'),
    path('deletedivision/<int:id>/', views.delete_division, name='delete-division'),

    path('grades', views.GradeListView.as_view(), name='grades-list'),
    path('addgrade', views.GradeAddForm.as_view(), name='add-grade'),
    path('deletegrade/<int:id>/', views.delete_grade, name='delete-grade'),

    path('acyear', views.AcademicYearListView.as_view(), name='acyear-list'),
    path('addacyear', views.AcademicYearAddForm.as_view(), name='add-acyear'),
    path('deleteacyear/<int:id>/', views.delete_acyear, name='delete-acyear'),
]