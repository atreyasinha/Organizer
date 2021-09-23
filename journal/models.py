from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Journal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=20)
    entry = models.CharField(max_length=20000)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.description
