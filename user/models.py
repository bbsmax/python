from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(blank=True, null=True)
    bio = models.TextField(default="", blank=True)
    superhost = models.BooleanField(default=False, blank=True)
    pass
