from django.shortcuts import render
from .models import Team

teams = Team.objects.all()
data = {
    'teams': teams,
}

def home(request):
    return render(request, 'pages/home.html', data)



def about(request):
    return render(request, 'pages/about.html', data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')
