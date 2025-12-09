from django.db import models
from django.contrib.auth.models import User

class TaskStatus(models.TextChoices):
    INCOMPLETE = 'INCOMPLETE'
    COMPLETE = 'COMPLETE'

    @classmethod
    def choices(cls):
        return [(c.value, c.value.capitalize()) for c in cls]

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=15,
        choices=TaskStatus.choices,
        default=TaskStatus.INCOMPLETE
    )
    due_date = models.DateField(null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title