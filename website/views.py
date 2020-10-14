from django.shortcuts import render, get_list_or_404
from .models import Main


def home(request):

    site = Main.objects.all()

    return render(request, 'home.html', {'site': site})

def about(request):
    
    siteabout = Main.objects.get()

    return render(request, 'about.html', {'siteabout': siteabout})


def features(request):

    return render(request, 'features.html')