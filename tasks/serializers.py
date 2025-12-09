from rest_framework import serializers
from .models import Task, TaskStatus


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    def validate_status(self, value):
        if value not in TaskStatus.values:
            raise serializers.ValidationError("Invalid status")
        return value

    class Meta:
        model = Task
        fields = "__all__"