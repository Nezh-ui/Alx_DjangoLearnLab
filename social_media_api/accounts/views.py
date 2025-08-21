from multiprocessing.managers import Token
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer


# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get_or_create(user=user)
            return Response({'user': UserRegistrationSerializer(user).data, 'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get_or_create(user=user)
            return Response({'user': UserLoginSerializer(user).data, 'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(APIView):
    def get(self, request):
        user = request.user
        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FollowView(generics.GenericAPIView): # handles following users
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()

    def post(self, request):
        try:
            user = request.user
            follow_user_id = request.data.get('follow_user_id')
            follow_user = CustomUser.objects.get(id=follow_user_id)
            user.follow(follow_user)
            return Response({'message': 'Successfully followed user.'}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

class UnfollowView(generics.GenericAPIView): # handles unfollowing users
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()

    def post(self, request):
        try:
            user = request.user
            unfollow_user_id = request.data.get('unfollow_user_id')
            unfollow_user = CustomUser.objects.get(id=unfollow_user_id)
            user.unfollow(unfollow_user)
            return Response({'message': 'Successfully unfollowed user.'}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
