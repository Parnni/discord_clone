from django.contrib.auth.models import User
from django.db import models


class BaseAudits(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Room(BaseAudits):
    # host =
    # topic =
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="messages")
    body = models.TextField()

    class Meta:
        ordering = ["-created"]
        verbose_name = "Message"
        verbose_name_plural = "Messages"
