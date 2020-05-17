from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 100)
    blog_date = models.DateField()
    description = models.CharField(max_length = 250)
    