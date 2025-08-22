from django.shortcuts import render
from rest_framework import generics
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.response import Response


# Create your views here.
class NotificationListView(generics.ListAPIView): # ListAPIView for notification list
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def get(self, request):
        all_notifications = Notification.objects.all()
        unread_notifications = all_notifications.filter(is_read=False)
        serializer = NotificationSerializer(unread_notifications, many=True)
        return Response(serializer.data)