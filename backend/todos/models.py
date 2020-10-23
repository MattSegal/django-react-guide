from django.db import models
from django.utils import timezone

class Todo(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=128)
