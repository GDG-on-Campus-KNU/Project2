from rest_framework import serializers
from .models import Board
from django.contrib.auth.models import User


class BoardSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Board
        fields = ['id', 'owner', 'category', 'image', 'createdAt', 'updatedAt', 'content',
                  'likeCount', 'votedIndex', 'voteText', 'voteTotal', 'currentUser']
