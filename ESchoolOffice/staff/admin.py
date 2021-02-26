from django.contrib import admin
from .models import *


class DesignationAdmin(admin.ModelAdmin):
    fields = [ 'desig_name' ]


admin.site.register(Designation, DesignationAdmin)