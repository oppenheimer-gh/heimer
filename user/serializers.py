from rest_framework import serializers

from user.models import User, Mentor


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'profile_photo_url',
            'email',
            'is_mentor',
        )

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'profile_photo_url',
            'email',
            'is_mentor',
        )


class MentorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    get_mentees = serializers.StringRelatedField(many=True)

    class Meta:
        model = Mentor
        fields = (
            'user',
            'is_available',
            'get_mentees',
        )


class MenteeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    mentor = MentorSerializer(read_only=True)

    class Meta:
        model = Mentor
        fields = (
            'user',
            'mentor',
        )
