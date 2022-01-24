from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    emails = models.CharField(max_length=500, null=True, blank=True)
    shortIntro = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profileImage = models.ImageField(null=True, blank=True, upload_to='profiles/', default='profiles/user-default.png')
    socialGithub = models.CharField(max_length=200, null=True, blank=True)
    socialTwitter = models.CharField(max_length=200, null=True, blank=True)
    socialLinkedin = models.CharField(max_length=200, null=True, blank=True)
    socialYoutube = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return str(self.user.username)