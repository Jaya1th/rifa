from django.db import models

class Employee(models.Model):
    employee_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    grade = models.CharField(max_length=5)
    practice = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    project_manager = models.CharField(max_length=100)
    delivery_manager = models.CharField(max_length=100)
    business_leader = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.employee_id})"

class Course(models.Model):
    course_id = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name

class Enrollment(models.Model):
    employee_id = models.CharField(max_length=20)
    course_id = models.CharField(max_length=100)
    progress = models.IntegerField(default=0)  # 0 to 100
    status = models.CharField(max_length=20, default='Not Completed')  # Completed / Not Completed

    def __str__(self):
        return f"{self.employee_id} - {self.course_id} - {self.status}"
