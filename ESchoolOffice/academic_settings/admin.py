from django.contrib import admin

from .models import Subject, Standard, Division, AcademicYear, ExamDetail,Grade
# Register your models here.

admin.site.register(Subject)
admin.site.register(Standard)
admin.site.register(Division)
admin.site.register(AcademicYear)
admin.site.register(ExamDetail)
admin.site.register(Grade)
