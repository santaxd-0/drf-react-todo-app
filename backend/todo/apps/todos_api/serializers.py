from rest_framework import serializers

from .models import Task, Category

class TaskAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "description", "date_created", "status", "related_category"]

class CategoryAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]