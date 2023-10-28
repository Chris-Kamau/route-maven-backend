from rest_framework import serializers
from .models import Todo, Staff

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

class user_serializer(serializers.ModelSerializer):

    class Meta:
        model = Staff
        fields = '__all__'
