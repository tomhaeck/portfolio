from django.contrib import admin

from projects.models import Project, ProjectImage, Category

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    fields = ("image",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at", "category")
    list_filter = ("category",)

    search_fields = ("title", "description")
    inlines = [ProjectImageInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
