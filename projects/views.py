from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
projectslist = [
        {
            'id':'1',
            'title':'Blog website',
            'description':'Site about cloud computing blogs',
        },
        {
            'id':'2',
            'title':'Portfolio',
            'description':'Site to showcase self'
        },
        {
            'id':'3',
            'title':'Ecommerce',
            'description':'Fully functional ecommerce site'
        }        
    ]

def projects(request):
    msg = "Projects"
    num = 10

    content = {'message':msg,
    'number':num,
    'projects':projectslist
    }
    return render(request, 'projects/projects.html', content)

def project(request, pk):
    projectObj = None
    for i in projectslist:
        if i['id'] == pk:
           projectObj = i

    content = {'project':projectObj}
    return render(request, 'projects/single-project.html', content)
    
