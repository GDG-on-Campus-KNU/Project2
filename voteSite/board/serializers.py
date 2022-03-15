from rest_framework import serializers
from .models import Board, Choice


class BoardSerializer(serializers.ModelSerializer):
    serializer_class = BoardSerializer

    class Meta:
        model = Board
        fields = ['author', 'category', 'createdAt', 'updatedAt', 'content', 'recommend','choiceList']
