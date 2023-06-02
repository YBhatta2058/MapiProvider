from django.db import models

# Create your models here.
class BlogDB(models.Model):
    title = models.CharField(max_length = 30)
    img = models.ImageField('Label',upload_to = "./holdApi/images/",default = "")
    content = models.TextField(default = "")