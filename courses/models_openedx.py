from django.db import models

class OpenEdxUser(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.EmailField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class StudentCourseEnrollment(models.Model):
    user_id = models.IntegerField()
    course_id = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'student_courseenrollment'
