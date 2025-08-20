# serializers.py
from rest_framework import serializers
from notifications.models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField()  # show username instead of ID

    class Meta:
        model = Notification
        fields = ['id', 'actor', 'verb', 'target', 'unread', 'timestamp']
