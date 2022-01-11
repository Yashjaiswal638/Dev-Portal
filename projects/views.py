from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def projects(request):
    msg = "Projects"
    num = 10
    content = {'message':msg,
    'number':num,
    }
    return render(request, 'projects/projects.html', content)

def project(request, pk):
    return render(request, 'projects/single-project.html')
    
