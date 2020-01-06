from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Post(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
