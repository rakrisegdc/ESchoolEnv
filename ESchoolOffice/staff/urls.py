from django.urls import path
from . import views


urlpatterns = [
    path('designation/', views.designation),
    path('leavetype/', views.leavetype),
    path('staff/', views.staff),
    path('staffleave/', views.staffleave),
    path('teachersubjects', views.teachersubjects),
]