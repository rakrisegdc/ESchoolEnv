from django.urls import path

from . import views

app_name = 'pta'
urlpatterns = [
    path('des_create', views.PTADesignationForm.as_view(), name='pta_des_create'),
    path('des_index', views.PTADesignationList.as_view(), name='pta_des_index'),
    path('des/<int:pk>/', views.PTADesignationView.as_view(), name='pta_des_detail'),
    path('des_delete/<int:pk>/', views.PTADesignationDelete.as_view(), name='pta_des_delete'),
    path('des_update/<int:pk>/', views.PTADesignationUpdate.as_view(), name='pta_des_update'),
    path('reg/create', views.CommitteeRegistrationForm.as_view(), name='pta_reg_create'),
    path('reg/index', views.CommitteeRegistrationList.as_view(), name='pta_reg_index'),
    path('reg/update/<int:pk>/', views.CommitteeRegistrationUpdate.as_view(), name='pta_reg_update'),
    path('reg/delete/<int:pk>/', views.CommitteeRegistrationDelete.as_view(), name='pta_reg_delete'),
    path('reg/view/<int:pk>/', views.CommitteeRegistrationView.as_view(), name='pta_reg_view'),

]