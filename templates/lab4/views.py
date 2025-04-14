from django.shortcuts import render


def index(request):
    """Головна сторінка з посиланнями на всі інші сторінки"""
    return render(request, 'lab4/main_page.html')


def about(request):
    """Сторінка з інформацією про проєкт"""
    return render(request, 'lab4/about.html')


def contact(request):
    """Сторінка з контактною інформацією"""
    return render(request, 'lab4/contact.html')


def projects(request):
    """Сторінка зі списком проєктів"""
    return render(request, 'lab4/projects.html')


def services(request):
    """Сторінка з переліком послуг"""
    return render(request, 'lab4/services.html')