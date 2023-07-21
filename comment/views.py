from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from comment.models import Comment
from comment.serializers import CreateCommentSerializer, CommentSerializer
from post.models import Post
from post.serializers import PostSerializer
from user.serializers import UserSerializer


class CommentPagination(PageNumberPagination):
    page_size = 5  # default number of objects per page if 'limit' query param is not set.
    page_size_query_param = 'limit'
    max_page_size = 100  # Max limit value


class GetCreateCommentAPIView(GenericAPIView):
    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated,]
        elif self.request.method == 'GET':
            self.permission_classes = [AllowAny,]
        return super(GetCreateCommentAPIView, self).get_permissions()

    serializer_class = CreateCommentSerializer
    pagination_class = CommentPagination

    def post(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.is_valid():
            user_serializer = UserSerializer(request.user)
            post_serializer = PostSerializer(post)
            serializer.save(user=request.user, post=post)
            post.comments_count += 1
            post.save()
            return Response({
                'comment': serializer.data,
                'user': user_serializer.data,
                'post': post_serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, post_id):
        comments = Comment.objects.filter(post=post_id).order_by('created_at')
        page = self.paginate_queryset(comments)

        if page:
            serializer = CommentSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = CommentSerializer(comments, many=True)
        return Response({
            'comments': serializer.data
        }, status=status.HTTP_200_OK)


class DeleteCommentAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, comment_id):
        try:
            comment = Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            return Response({'error': 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)

        if comment.user != request.user:
            return Response({'error': 'You are not allowed to delete this comment'}, status=status.HTTP_403_FORBIDDEN)

        post = comment.post
        post.comments_count -= 1
        post.save()
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
