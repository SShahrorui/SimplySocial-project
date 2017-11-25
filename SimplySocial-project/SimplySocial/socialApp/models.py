from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE, related_name='profile')
    profile_pic= models.ImageField(upload_to='profile_pic')
    bio=models.CharField(max_length=255)
    website=models.URLField()
