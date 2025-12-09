from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwnerOrAdmin


class TaskViewSet(viewsets.ModelViewSet):
    """
    This allows CRUD operations on Tasks
    """
    serializer_class = TaskSerializer
    permission_classes = (IsOwnerOrAdmin)

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Task.objects.all()
        return Task.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=["post"])
    def toggle(self, request, pk=None):
        """
        Call it like this POST /api/tasks/<id>/toggle/
        it toggles task status
        """
        task = self.get_object()
        task.status = not task.status
        task.save()
        return Response(self.get_serializer(task).data)