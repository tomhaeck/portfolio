from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    color = models.CharField(max_length=7, help_text="Color hex code of the project, e.g. #abcdef")

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    cover_image = models.ImageField(upload_to="projects/covers/", blank=True, null=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    categories = models.ManyToManyField(Category,
                                        related_name="projects",
                                        null=True,
                                        blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


def project_image_upload_to(instance, filename):
    return f"projects/{instance.project_id}/{filename}"

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to=project_image_upload_to)
