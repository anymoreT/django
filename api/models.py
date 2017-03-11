from django.db import models

# Create your models here.

class Poem(models.Model):
    author = models.CharField(max_length = 50)
    title =  models.CharField(max_length = 50)
    type = models.CharField(max_length = 50)
    date = models.DateField(auto_now = True)
