from django.shortcuts import render, get_object_or_404
from .models import University, Specialty, EducationalProgram

# Список университетов
def university_list(request):
    universities = University.objects.all()
    return render(request, 'main/university_list.html', {'universities': universities})

# Информация об университете и список специальностей
def university_detail(request, university_id):
    university = get_object_or_404(University, pk=university_id)
    specialties = university.specialties.all()
    return render(request, 'main/university_detail.html', {'university': university, 'specialties': specialties})

def specialty_list(request):
    specialties = Specialty.objects.prefetch_related('universities')
    return render(request, 'main/specialty_list.html', {'specialties': specialties})

# Информация по специальности и список образовательных программ
def specialty_detail(request, specialty_id):
    specialty = get_object_or_404(Specialty, pk=specialty_id)
    programs = specialty.educationalprogram_set.all()
    return render(request, 'main/specialty_detail.html', {'specialty': specialty, 'programs': programs})

# Информация по образовательной программе
def program_detail(request, program_id):
    program = get_object_or_404(EducationalProgram, pk=program_id)
    return render(request, 'main/program_detail.html', {'program': program})
