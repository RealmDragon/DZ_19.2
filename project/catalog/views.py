from django.shortcuts import render

def home(request):
    return render(request, 'catalog/templates/home.html')

def contact(request):
    return render(request, 'catalog/templates/contact.html')

def index(request):
    return render(request, 'catalog/templates/index.html')
