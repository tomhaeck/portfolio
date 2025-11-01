from django.urls import path
from projects import views
urlpatterns = [
    path("", views.all_projects, name="all_projects"),
    path("<int:id>/", views.project_detail, name="project_detail"),
]
