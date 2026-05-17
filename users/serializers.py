from rest_framework import serializers


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        from users.models import Organization

        model = Organization
        fields = ["id", "name", "created_at", "updated_at"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        from django.contrib.auth.models import User

        model = User
        fields = ["id", "username", "email", "organization", "created_at", "updated_at"]
