from django.db import models
from django.contrib.auth.models import User

# Университет
class University(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    description = models.TextField()

# Специальность
class Specialty(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # university = models.ForeignKey(University, on_delete=models.CASCADE)
    universities = models.ManyToManyField(University, related_name='specialties')

# Образовательная программа
class EducationalProgram(models.Model):
    name = models.CharField(max_length=100)
    requirements = models.TextField()
    min_score = models.IntegerField()
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)

# Студент (admin - Admin12345)
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saved_programs = models.ManyToManyField(EducationalProgram, blank=True)
