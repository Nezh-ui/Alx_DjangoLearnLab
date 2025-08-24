from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from posts.models import Post
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.
class Notification(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='actor_notifications')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='notifications')
    verb = models.CharField(max_length=255)  # Verb describing the action (e.g., "liked", "commented")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    target = GenericForeignKey('content_type', 'object_id') # The object that the action was performed on (e.g., Comment)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"Notification for {self.recipient} on {self.post.title}"
