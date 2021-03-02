from django.contrib import admin
from .models import *

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Admission Details', { 'fields' : [
            'stud_admno',
            'standard',
            'stud_regdate'
        ]}),

        ('Personal Details Student', { 'fields' : [
            'stud_name',
            'stud_address',
            'state',
            'stud_email',
            'stud_adharno',
            'religion',
            'caste',
            'stud_nationality',
            'mothertongue',
            'stud_dob',
            'stud_guardian',
            'stud_bloodgroup',
            'stud_gender'
        ]}),
    ]


admin.site.register(Student, StudentAdmin)

admin.site.register(Parent)