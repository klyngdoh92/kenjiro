from rest_framework import generics, permissions, status
from rest_framework.response import Response

from users.serializers import OrganizationSerializer, UserSerializer


class CreateOrganizationView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrganizationSerializer

    def post(self, request, *args, **kwargs):
        # Logic to create an organization
        return Response(
            {"message": "Organization created successfully"},
            status=status.HTTP_201_CREATED,
        )


class CreateUserView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        # Logic to create a user
        return Response(
            {"message": "User created successfully"}, status=status.HTTP_201_CREATED
        )
