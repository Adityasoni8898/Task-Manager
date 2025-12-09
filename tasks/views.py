from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwnerOrAdmin
from .paginations import CustomListPagination
from .models import TaskStatus
from rest_framework.exceptions import PermissionDenied


class TaskViewSet(viewsets.ModelViewSet):
    """
    This allows CRUD operations on Tasks
    """
    serializer_class = TaskSerializer
    permission_classes = (IsOwnerOrAdmin,)
    pagination_class = CustomListPagination

    def get_queryset(self):
        user = self.request.user

        queryset = Task.objects.all() if user.is_staff else Task.objects.filter(owner=user)

        # filter by status
        status_param = self.request.query_params.get("status")
        if status_param in TaskStatus.values:
            queryset = queryset.filter(status=status_param)

        # filter by owner, only for staff
        owner_param = self.request.query_params.get("owner")

        if owner_param:
            if not user.is_staff:
                raise PermissionDenied("You do not have permission to filter by owner.")

            queryset = queryset.filter(owner__username=owner_param)

        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=["post"])
    def toggle(self, request, pk=None):
        """
        Call it like this POST /api/tasks/<id>/toggle/
        it toggles task status
        """
        task = self.get_object()
        task.status = (
            TaskStatus.COMPLETE
            if task.status == TaskStatus.INCOMPLETE
            else TaskStatus.INCOMPLETE
        )
        task.save()
        return Response(self.get_serializer(task).data)