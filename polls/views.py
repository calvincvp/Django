from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def page1(request): 
    return render(request, 'page1.html')

def planets(request): 
    return render(request, 'planets.html')

def aniwords(request): 
    return render(request, 'aniwords.html')

def xraycarousels(request): 
    return render(request, 'x-raycarousels.html')

def event(request):
    return render(request, 'event.html')

def james(request): 
    return render(request, 'Jamescarousels.html')

def hubble(request): 
    return render(request, 'hubble.html')






# Create your views here.
