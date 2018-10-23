from django.db import models

# Create your models here.

class Notice(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=200)
    c_date = models.DateTimeField()