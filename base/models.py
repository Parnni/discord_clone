from django.contrib.auth.models import User
from django.db import models


class BaseAudits(models.Model):
    """Base model for audits."""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Topic(models.Model):
    """Model for managing topics."""

    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Room(BaseAudits):
    """Model for managing the chat rooms."""

    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    # participants =

    class Meta:
        ordering = ["-created"]
        verbose_name = "Room"
        verbose_name_plural = "Rooms"

    def __str__(self):
        # return f"Host: {self.host} - Topic: {self.topic} , Name: {self.name}"
        return f"Name: {self.name}"


class Message(BaseAudits):
    """Model for managing the messages."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="messages")
    body = models.TextField()

    class Meta:
        ordering = ["-created"]
        verbose_name = "Message"
        verbose_name_plural = "Messages"
