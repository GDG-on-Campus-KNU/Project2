from rest_framework import serializers
from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ['id', 'title', 'code', 'owner', 'boardId']




