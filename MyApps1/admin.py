from django.contrib import admin
from MyApps1.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','job','sal','addr']

admin.site.register(Employee,EmployeeAdmin)
