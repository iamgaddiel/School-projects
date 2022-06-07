from uuid import uuid4
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField(User, related_name='friends')

    def __str__(self) -> str:
        return f'{self.user.username} friends'

class Message(models.Model):
    id = models.UUIDField(default=uuid4, unique=True, editable=False, primary_key=True)
    message = models.TextField()
    _from = models.ForeignKey(User, on_delete=models.CASCADE)
    to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_to')
    timestamp = models.DateTimeField(auto_now=now)

    def __str__(self) -> str:
        return f'{self._from} -> {self.to} - {self.timestamp}'
    
    class Meta:
        ordering = ['-timestamp']

