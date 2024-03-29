from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    CATEGORY = (
        ('Food','Food'),
        ('Clothing', 'Clothing'),
        ('Housing','Housing'),
        ('Education','Education'),
        ('Entertainment','Entertainment'),
        ('Other','Other'),
    )

    category = models.CharField(max_length=200,choices=CATEGORY, default='Education')

    projected = models.IntegerField(default=0)
    actual = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.description
