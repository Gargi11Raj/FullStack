from django.db import models
from datetime import datetime, date

# Create your models here.

class All_Photos(models.Model):
    name = models.CharField (max_length=150)
    img = models.ImageField(upload_to='pics')
    kab = models.DateField(auto_now=True)
    dekha = models.IntegerField()
    pdf = models.FileField(upload_to='files', default='Null')
