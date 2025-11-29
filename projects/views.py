from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from projects.models import Project

# Create your views here.
def all_projects(request):
    projects = Project.objects.all().order_by("-created_at")
    if contains:=request.GET.get("contains"):
        projects = projects.filter(Q(title__icontains=contains) | Q(description__icontains=contains))

    return render(request, "projects/all_projects.html", {"projects":projects})


def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, "projects/project_detail.html", {"project":project})


def about_me(request):
    return render(request, "projects/about_me.html")