from django.contrib import admin

from users.models import Membership, Organization


class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 1


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    search_fields = ("name",)
    inlines = [MembershipInline]


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "organization", "role")
    list_filter = ("role", "organization")
    search_fields = ("user__username", "organization__name")
