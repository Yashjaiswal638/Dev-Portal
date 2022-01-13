from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def projects(request):
    projects = models.Project.objects.all()
    content = {'projects':projects}
    return render(request, 'projects/projects.html', content)

def project(request, pk):
    projectObj = models.Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    content = {'project': projectObj, 
        'tags': tags
    }
    return render(request, 'projects/single-project.html', content)
    
