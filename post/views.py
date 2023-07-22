from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from post.models import Post
from post.serializers import CreatePostSerializer, PostSerializer
from user.serializers import UserSerializer, MentorListSerializer


class CreatePostAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    serializer_class = CreatePostSerializer

    def post(self, request):
        if Post.objects.filter(user=request.user).exists():
            return Response({'error': 'User already has a post'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.is_valid():
            user_serializer = UserSerializer(request.user)
            serializer.save(user=request.user)
            return Response({
                'post': serializer.data,
                'user': user_serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetAllPostAPIView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response({
            'posts': serializer.data
        }, status=status.HTTP_200_OK)


class GetPostAPIView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PostSerializer(post)
        return Response({
            'post': serializer.data
        }, status=status.HTTP_200_OK)


class DeletePostAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

        if post.user != request.user:
            return Response({'error': 'You are not the owner of this post'}, status=status.HTTP_401_UNAUTHORIZED)

        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AvailableMentorView(GenericAPIView):
    def get(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        available_mentors = post.available_mentors
        serializer = MentorListSerializer(available_mentors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)