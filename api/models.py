from django.db import models
from django.utils import timezone

# Create your models here.

class Poem(models.Model):
    author = models.CharField(max_length = 50)
    title =  models.CharField(max_length = 50)
    type = models.CharField(max_length = 50)
    date = models.DateField(auto_now = True)


class MyModel(models.Model):

    file = models.ImageField(upload_to=u'photos')
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return u"photo {0}".format(self.file.url)

# Create your models here.
class ResourceModel(models.Model):
        id = models.AutoField(primary_key=True)
        resource_id = models.CharField(max_length=50, db_index=True, unique=True)
        resource_remark = models.CharField(max_length=50)