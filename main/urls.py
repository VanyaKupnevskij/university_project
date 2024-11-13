from django.urls import path
from . import views

urlpatterns = [
    path('universities/', views.university_list, name='university_list'),
    path('universities/<int:university_id>/', views.university_detail, name='university_detail'),
    path('specialties/', views.specialty_list, name='specialty_list'),
    path('specialties/<int:specialty_id>/', views.specialty_detail, name='specialty_detail'),
    path('programs/<int:program_id>/', views.program_detail, name='program_detail'),
]
