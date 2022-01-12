from django.db import models
import uuid

# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    demoLink = models.CharField(max_length=1500, null=True, blank=True)
    sourceLink = models.CharField(max_length=1500, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
