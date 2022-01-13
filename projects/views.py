from django.shortcuts import render
from django.http import HttpResponse
from . import models
from .forms import ProjectForm

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
    

def createProject(request):
    form = ProjectForm()
    context = {'form': form}
    return render(request, "projects/project_form.html", context)