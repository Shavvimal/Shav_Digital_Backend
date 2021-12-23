from django.db import models
from datetime import datetime


class ContactPost(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.email
