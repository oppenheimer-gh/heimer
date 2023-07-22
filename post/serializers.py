from rest_framework import serializers

from post.models import Post
from user.serializers import UserSerializer, MentorListSerializer


class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'source_latitude',
            'source_longitude',
            'source_country',
            'destination_latitude',
            'destination_longitude',
            'destination_country',
            'message',
        )

    def create(self, validated_data):
        return Post.objects.create(**validated_data)


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    available_mentors = MentorListSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'created_at',
            'source_latitude',
            'source_longitude',
            'source_country',
            'destination_latitude',
            'destination_longitude',
            'destination_country',
            'message',
            'distance_in_km',
            'comments_count',
            'available_mentors',
            'user',
        )
