from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'staff'

urlpatterns = [
    url(r'designation/', views.designation, name="designation"),
    url(r'leavetype/', views.leavetype, name="leaveType"),
    url(r'', views.staff, name="staffDetails"),
]