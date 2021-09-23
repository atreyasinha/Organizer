from rest_framework import serializers
from .models import Budget

class BudgetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['category']