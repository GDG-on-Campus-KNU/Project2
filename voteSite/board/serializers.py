from rest_framework import serializers
from .models import Board
from django.contrib.auth.models import User


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['author', 'category', 'createdAt', 'updatedAt', 'content', 'recommend']


class UserSerializer(serializers.ModelSerializer):
    boards = serializers.PrimaryKeyRelatedField(many=True, queryset=Board.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = ['id', 'username', 'boards', 'owner']
