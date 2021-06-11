from django.db import models
from django.contrib.auth.models import User


class Parks(models.Model):
  name=models.CharField(max_length=100)
  images=models.ImageField(upload_to='park_photo', blank=True)
  description=models.TextField(max_length=1000)
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  date = models.DateTimeField(auto_now=True)
