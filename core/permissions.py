from rest_framework.permissions import BasePermission


class IsOrgAdmin(BasePermission):
    def has_permission(self, request, view):
        from users.models import Membership

        org_id = request.data.get("organization")

        return Membership.objects.filter(
            user=request.user, organization_id=org_id, role="admin"
        ).exists()
