from django.db import models
from django.utils import timezone

class Post(models.Model):
  author = models.ForeignKey('auth.User')
  title = models.CharField(max_length=200)
  text = models.Textfield()
  created_date = models.DateTimeField(
    
