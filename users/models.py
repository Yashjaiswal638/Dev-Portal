from django.db import models
from django.contrib.auth.models import User
import uuid

from django.db.models.signals import post_save, post_delete

from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    emails = models.CharField(max_length=500, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    shortIntro = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    profileImage = models.ImageField(
        null=True, blank=True, upload_to='profiles/',
        default='profiles/user-default.png')
    socialGithub = models.CharField(max_length=200, null=True, blank=True)
    socialTwitter = models.CharField(max_length=200, null=True, blank=True)
    socialLinkedin = models.CharField(max_length=200, null=True, blank=True)
    socialYoutube = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return str(self.username)


class Skill(models.Model):
    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, 
        unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.name)

# @receiver(post_save, sender = Profile)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            emails=user.email,
            name=user.first_name,
        )


# @receiver(post_delete, sender = Profile)
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)



