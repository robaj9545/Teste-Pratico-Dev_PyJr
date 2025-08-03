from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    task_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'color', 'created_at', 'updated_at', 'task_count']
        read_only_fields = ['created_at', 'updated_at']

    def get_task_count(self, obj):
        return obj.task_set.count()