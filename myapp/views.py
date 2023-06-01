from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render,redirect, get_object_or_404 
from .forms import CreateNewTask,CreateNewProject
# Create your views here.

def index(request):
    title = 'Welcome to Django Course !!'
    return render(request, 'index.html',{
        'title':title
    })

def hello(request, username):
    return HttpResponse("<H1>Hello %s</H1>" % username)

def about(request):
    username = 'Adrian'
    return render(request, 'about.html', {
        'username':username
    })

def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html',{
        'projects':projects
    })


def task(request):
    # task = Task.objects.get(id=id)
    # task = get_object_or_404(Task,id=id)
    tasks = Task.objects.all()
    return render(request,'tasks/tasks.html', {
        'tasks':tasks
    })

def create_task(request):
    if request.method == 'GET':
        return render(request,'tasks/create_task.html',{
        'form': CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'],description=request.POST['description'],project_id=2)
        return redirect(task)

def create_project(request):
    if request.method == 'GET':    
        return render(request, 'projects/create_project.html',{
        'form': CreateNewProject()
        })
    else:
        project = Project.objects.create(name=request.POST['name'])
        return redirect(projects)
    
def project_detail(request,id):
    project = get_object_or_404(Project, id=id)
    task = Task.objects.filter(project_id=id)
    return render(request,'projects/project_detail.html',{
        'project':project,
        'task':task,
    })