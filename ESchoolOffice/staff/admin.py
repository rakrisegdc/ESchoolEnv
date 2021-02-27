from django.contrib import admin
from .models import *


class DesignationAdmin(admin.ModelAdmin):
    fields = ['desig_name']


class LeaveTypeAdmin(admin.ModelAdmin):
    fields = ['leave_type']


class StaffAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Staff Details', { 'fields' : ['staff_name',
                                        'staff_address',
                                        'staff_contactno',
                                        'staff_email',
                                        'staff_dob']}),

        ('Institution Details of Staff', { 'fields' : ['staff_doj',
                                                       'staff_status',
                                                       'desig_id',
                                                       'staff_adharno',
                                                       'staff_active']}),
    ]


class TeacherSubjectAdmin(admin.ModelAdmin):
    fields = ['subject_id', 'teacher_id']


admin.site.register(Designation, DesignationAdmin)
admin.site.register(LeaveType, LeaveTypeAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(TeacherSubjects, TeacherSubjectAdmin)