from rest_framework import serializers
from .models import Task
from categories.serializers import CategorySerializer

class TaskSerializer(serializers.ModelSerializer):
    category_detail = CategorySerializer(source='category', read_only=True)
    owner_name = serializers.CharField(source='owner.username', read_only=True)
    shared_with_details = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'completed', 'priority', 
            'due_date', 'created_at', 'updated_at', 'owner', 'owner_name',
            'category', 'category_detail', 'shared_with', 'shared_with_details'
        ]
        read_only_fields = ['owner', 'created_at', 'updated_at']

    def get_shared_with_details(self, obj):
        return [{'id': user.id, 'username': user.username} for user in obj.shared_with.all()]

    def create(self, validated_data):
        shared_with_data = validated_data.pop('shared_with', [])
        task = Task.objects.create(**validated_data)
        task.shared_with.set(shared_with_data)
        return task

    def update(self, instance, validated_data):
        shared_with_data = validated_data.pop('shared_with', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        if shared_with_data is not None:
            instance.shared_with.set(shared_with_data)
        
        return instance