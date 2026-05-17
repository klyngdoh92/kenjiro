from django.urls import path

from core import views

urlpatterns = [
    path("projects", views.ListCreateProjectView.as_view()),
    path("projects/<int:project_id>", views.RetrieveUpdateDestroyProjectView.as_view()),
    path("tasks", views.ListCreateTaskView.as_view()),
    path("tasks/<int:task_id>", views.RetrieveUpdateDestroyTaskView.as_view()),
    path("health/", views.HealthCheckAPIVIew.as_view())
]
