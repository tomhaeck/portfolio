from django.shortcuts import render, get_object_or_404

from projects.models import Project

# Create your views here.
def all_projects(request):
    projects = Project.objects.all()
    return render(request, "projects/all_projects.html", {"projects":projects})


def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, "projects/project_detail.html", {"project":project})
