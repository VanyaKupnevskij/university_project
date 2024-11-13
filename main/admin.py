from django.contrib import admin
from .models import University, Specialty, EducationalProgram, Student

admin.site.register(University)
admin.site.register(Specialty)
admin.site.register(EducationalProgram)
admin.site.register(Student)
