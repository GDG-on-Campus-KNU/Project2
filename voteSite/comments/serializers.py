from rest_framework import serializers
from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    board_id = serializers.ReadOnlyField()

    class Meta:
        model = Comment
        fields = ['id', 'title', 'code', 'owner', 'board_id']




