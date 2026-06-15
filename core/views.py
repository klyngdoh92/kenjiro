from rest_framework import generics, permissions
from rest_framework.response import Response

from core.permissions import IsOrgAdmin
from core.serializers import ProjectSerializer, TaskSerializer


class ListCreateProjectView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProjectSerializer

    def get_queryset(self):
        from core.models import Project

        return Project.objects.filter(organization__membership__user=self.request.user)


class RetrieveUpdateDestroyProjectView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProjectSerializer
    lookup_url_kwarg = "project_id"

    def get_queryset(self):
        from core.models import Project

        return Project.objects.filter(organization__membership__user=self.request.user)


class ListCreateTaskView(generics.ListCreateAPIView):
    permission_classes = [IsOrgAdmin]
    serializer_class = TaskSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsOrgAdmin()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        query_params = self.request.query_params
        project_id = query_params.get("project")
        from core.models import Task

        if project_id is not None:
            return Task.objects.filter(
                project__id=project_id,
                project__organization__membership__user=self.request.user,
            )
        return Task.objects.none()


class RetrieveUpdateDestroyTaskView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TaskSerializer
    lookup_url_kwarg = "task_id"

    def get_queryset(self):
        from core.models import Task

        return Task.objects.filter(
            project__organization__membership__user=self.request.user
        )


class HealthCheckAPIView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        from django.db import connection

        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
            return Response({"status": "ok"})
        except Exception:
            return Response({"status": "error"}, status=500)
