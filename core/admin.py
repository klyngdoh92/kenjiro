from django.contrib import admin

from core.models import Project, Task


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "organization")
    list_filter = ("organization",)
    search_fields = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "project", "assigned_to")
    list_filter = ("project",)
    search_fields = ("title",)
