from rest_framework import serializers

from post.models import Post


class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'source_latitude',
            'source_longitude',
            'destination_latitude',
            'destination_longitude',
            'message',
        )
