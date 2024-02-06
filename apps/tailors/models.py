from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class TailorUser(AbstractUser):
    phone = models.CharField(max_length=15,blank=True, null=True)
    profile = models.ImageField(blank=True,upload_to='tailor_profiles/',default='default/profile-user.png')