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

class Group(models.Model):
    id = models.UUIDField(default=uuid4, unique=True, editable=False, primary_key=True)
    title = models.CharField(max_length=50, verbose_name='group name')
    slug = models.SlugField(verbose_name='group name')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    member = models.ManyToManyField(User, related_name='member', blank=True)
    image = models.ImageField(default='group_image.jpg', upload_to='group_images')
    timestamp = models.DateTimeField(auto_now=now)

    def __str__(self) -> str:
        return self.slug
    
    class Meta:
        ordering = ['-timestamp']

class GroupMessage(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    message = models.TextField(blank=True)
    _from = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=now)

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        ordering = ['-timestamp']

