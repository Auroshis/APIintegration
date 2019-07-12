from django.contrib import admin
from . models import employees

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'emp_id')
admin.site.register(employees, EmployeeAdmin)
