from django.db import models

# Create your models here.

#Table of Student
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    family_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=200)
    dob = models.DateField( auto_now=False, auto_now_add=False)
    email = models.EmailField()

    def __str__(self):
        return self.first_name 

#Table of Course
class Course(models.Model):
    course_name = models.CharField(max_length=50)

    def __str__(self):
        return self.course_name

#Table of Result
class Result(models.Model):
    course_selected_name = models.CharField(max_length=50)
    full_selected_name = models.CharField(max_length=160)
    score = models.CharField(max_length=10)

    def __str__(self):
        return f'Details:{self.course_selected_name} {self.full_selected_name} {self.score}'