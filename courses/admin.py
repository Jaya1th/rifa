from django.contrib import admin
from .models import Employee, Course, Enrollment

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'name', 'email', 'grade', 'practice', 'region', 'project_manager', 'delivery_manager', 'business_leader')
    search_fields = ('employee_id', 'name', 'email', 'grade', 'practice')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'course_name')
    search_fields = ('course_id', 'course_name')

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'course_id', 'progress', 'status')
    search_fields = ('employee_id', 'course_id')
