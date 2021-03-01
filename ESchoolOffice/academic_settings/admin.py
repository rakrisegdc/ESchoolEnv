from django.contrib import admin
from .models import *

class StandardAdmin(admin.ModelAdmin):
    fields = ['standard_name']

admin.site.register(Standard, StandardAdmin)