from rest_framework import serializers
from .models import Task

class TaskCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['category']