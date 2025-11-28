from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from projects import views

urlpatterns = ([
    path("", views.all_projects, name="all_projects"),
    path("<int:id>/", views.project_detail, name="project_detail"),
    path("about-me/", views.about_me, name="about_me"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
