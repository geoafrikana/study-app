from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from  embed_video.fields  import  EmbedVideoField

class CustomUser(AbstractUser):
    INSTRUCTOR = 'ins'
    STUDENT = 'stu'
    PORTAL_ROLES = [
       (INSTRUCTOR, 'Instructor'),
       (STUDENT, 'Student'),
    ]
    portal_role = models.CharField(max_length=15,
                                   choices=PORTAL_ROLES,
                                   default=STUDENT)

    def __str__(self):
        return self.username


class Course(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    instructor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,related_name='courses'
    )
    students = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='student_courses'
    )


class CourseContent(models.Model):
    title = models.CharField(max_length=250)
    content_video = EmbedVideoField()
    course = models.ForeignKey(Course, related_name='contents', on_delete=models.CASCADE)

class Assessment(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)


class Question(models.Model):
    title = models.CharField(max_length=300)
    Assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)


class Option(models.Model):
    text = models.CharField(max_length=300)
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    is_right = models.BooleanField(blank=False)


    





