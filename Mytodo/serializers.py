from dataclasses import fields
from enum import unique
from pyexpat import model
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    task = serializers.CharField(max_length=50)
    completed = serializers.BooleanField(default=False);
    description = serializers.CharField(max_length=200,default = "")



    def create(self,validated_data):
        return Todo.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.task = validated_data.get('task',instance.task)
        instance.completed = validated_data.get('completed',instance.completed)
        instance.description = validated_data.get('description',instance.description)
        instance.save()
        return instance