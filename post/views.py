from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from post.serializers import CreatePostSerializer


class CreatePostAPIView(GenericAPIView):
    serializer_class = CreatePostSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

