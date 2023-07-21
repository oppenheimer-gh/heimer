from rest_framework import serializers

from comment.models import Comment
from user.serializers import UserSerializer


class CreateCommentSerializer(serializers.ModelSerializer):
    message = serializers.CharField(max_length=255)

    class Meta:
        model = Comment
        fields = (
            'message',
        )

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = (
            'id',
            'created_at',
            'message',
            'user',
        )
