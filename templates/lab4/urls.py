from django.urls import path
from templates.lab4 import views

app_name = 'lab4'  # Простір імен для уникнення конфліктів з іншими додатками

urlpatterns = [
    path('', views.index, name='main_page'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
    path('services/', views.services, name='services'),
]