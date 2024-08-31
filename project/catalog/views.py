from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Убрали "catalog/templates"

def contact(request):
    return render(request, 'contact.html')  # Убрали "catalog/templates"

def index(request):
    return render(request, 'index.html')  # Убрали "catalog/templates"