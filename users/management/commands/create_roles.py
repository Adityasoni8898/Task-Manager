from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from tasks.models import Task


class Command(BaseCommand):
    help = "Create default roles: Admin and User, and assign permissions for Task model."

    def handle(self, *args, **options):
        # For creating groups
        admin_group, _ = Group.objects.get_or_create(name="Admin")
        user_group, _ = Group.objects.get_or_create(name="User")

        # Setting permissions for Task
        ct = ContentType.objects.get_for_model(Task)
        permissions = Permission.objects.filter(content_type=ct)

        # Admin has -> all task permissions
        for perm in permissions:
            admin_group.permissions.add(perm)

        # User has -> add, change, view (no delete)
        perms_for_user = permissions.filter(codename__in=["add_task", "change_task", "view_task"])  # type: ignore
        for perm in perms_for_user:
            user_group.permissions.add(perm)

        self.stdout.write(self.style.SUCCESS("Roles 'Admin' and 'User' created/updated."))