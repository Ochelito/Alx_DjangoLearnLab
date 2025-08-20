# views.py
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import NotificationSerializer
from notifications.models import Notification

class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only fetch notifications for logged-in user
        return Notification.objects.filter(recipient=self.request.user).order_by('-timestamp')

    @action(detail=False, methods=['post'])
    def mark_all_as_read(self, request):
        self.get_queryset().update(unread=False)
        return Response({"detail": "All notifications marked as read."}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def mark_as_read(self, request, pk=None):
        notification = get_object_or_404(self.get_queryset(), pk=pk)
        notification.unread = False
        notification.save()
        return Response({"detail": "Notification marked as read."}, status=status.HTTP_200_OK)
