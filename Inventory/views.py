from django.shortcuts import render
from .models import *

def Homepage(request):
    return render(request,'home.html')
def Aboutpage(request):
    return render(request,'about.html')
def Servicespage(request):
    return render(request,'services.html')
def Contactpage(request):
    return render(request,'contact.html')
def Peacock(request):
    return render(request,'peacock.html')