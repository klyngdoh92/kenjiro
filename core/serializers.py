from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        from core.models import Task

        model = Task
        fields = [
            "id",
            "project",
            "title",
            "description",
            "status",
            "assigned_to",
            "created_at",
            "updated_at",
        ]


class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True, source="task_set")

    class Meta:
        from core.models import Project

        model = Project
        fields = ["id", "name", "created_at", "updated_at", "tasks"]
