from django.urls import path

from . import views

app_name = 'pta'
urlpatterns = [
    path('des_create', views.PTADesignationForm.as_view(), name='des_create'),
    path('des_index', views.PTADesignationList.as_view(), name='des_index'),
    path('des/<int:pk>/', views.PTADesignationView.as_view(), name='des_detail'),
    path('reg_create', views.CommiteeRegistrationForm.as_view(), name='reg_create'),
    path('des_delete/<int:pk>/', views.PTADesignationDelete.as_view(), name='des_delete'),
    path('des_update/<int:pk>/', views.PTADesignationUpdate.as_view(), name='des_update'),
]