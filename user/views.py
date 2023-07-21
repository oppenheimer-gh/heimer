from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from user.serializers import RegisterSerializer, UserSerializer


class RegisterAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            # Return created user data along with token
            return Response({
                'user': serializer.data,
                'token': token.key
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'user': UserSerializer(user).data,
                'token': token.key
            }, status=status.HTTP_200_OK)
        else:
            return Response(
                {'error': 'Invalid username/password. Please try again.'}, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        Token.objects.filter(user=request.user).delete()
        logout(request)
        return Response({"status": "Successfully logged out."},
                        status=status.HTTP_200_OK)


class GetUserView(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({
            'user': serializer.data
        })
