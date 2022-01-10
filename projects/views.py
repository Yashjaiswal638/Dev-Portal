from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def projects(request):
    return HttpResponse('Following are the products')

def project(request, pk):
    return HttpResponse("<h2>Single Project</h2>")
    
