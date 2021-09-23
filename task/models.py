from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    """docstring forTask."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    CATEGORY = (
        ('Home','Home'),
        ('School', 'School'),
        ('Work','Work'),
        ('Self Improvement','Self Improvement'),
        ('Other','Other'),
    )

    category = models.CharField(max_length=200,choices=CATEGORY, default='Work')

    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.description
