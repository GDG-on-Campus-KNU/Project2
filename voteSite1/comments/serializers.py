from django.http import JsonResponse
from rest_framework import serializers
from comments.models import Comment, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']




