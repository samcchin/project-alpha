from django.shortcuts import render
from projects.models import Project

# Create your views here.


def list_projects(request):
    list_project = Project.objects.all()
    context = {
        "list_projects": list_project,
    }
    return render(request, "projects/list.html", context)
