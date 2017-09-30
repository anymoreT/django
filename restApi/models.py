from django.db import models

# Create your models here.

class RestApi(models.Model):
    apiName = models.CharField(max_length=50)
    contType = models.CharField(max_length=50)
    def __unicode__(self):
        return self.apiName
