from rest_framework import serializers

from user.models import User, Mentor, Mentee


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
            'has_posted'
        )


class MenteeForMentorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Mentee
        fields = (
            'user',
            'id',
        )


class MentorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    mentees = MenteeForMentorSerializer(read_only=True, many=True)
    mentees_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Mentor
        fields = (
            'user',
            'is_available',
            'mentees',
            'mentees_count',
            'id',
        )


class MentorListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    mentees_count = serializers.IntegerField(read_only=True)
    source_country = serializers.SerializerMethodField()
    source_country_code = serializers.SerializerMethodField()
    destination_country = serializers.SerializerMethodField()
    destination_country_code = serializers.SerializerMethodField()

    class Meta:
        model = Mentor
        fields = (
            'user',
            'mentees_count',
            'source_country',
            'source_country_code',
            'destination_country',
            'destination_country_code',
            'id'
        )

    def get_source_country(self, obj):
        post = obj.user.posts.first()
        return post.source_country if post else None

    def get_source_country_code(self, obj):
        post = obj.user.posts.first()
        return post.source_country_code if post else None

    def get_destination_country(self, obj):
        post = obj.user.posts.first()
        return post.destination_country if post else None

    def get_destination_country_code(self, obj):
        post = obj.user.posts.first()
        return post.destination_country_code if post else None


class MenteeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Mentee
        fields = (
            'user',
            'mentor_id',
            'id'
        )
