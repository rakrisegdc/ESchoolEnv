from django.contrib import admin
from .models import *


class DesignationAdmin(admin.ModelAdmin):
    fields = ['desig_name']


class LeaveTypeAdmin(admin.ModelAdmin):
    fields = ['leave_type']


admin.site.register(Designation, DesignationAdmin)
admin.site.register(LeaveType, LeaveTypeAdmin)