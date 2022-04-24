from django.contrib import admin
from .models import *


class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'grade_status')


class GradeAdmin(admin.ModelAdmin):
    list_display = ('position', 'salary')


admin.site.register(Grade, GradeAdmin)
admin.site.register(Staff, StaffAdmin)