from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User
from django.utils import timesince, timezone


class Post(models.Model):
    class Meta:
        ordering = ['-created_at']
        
    id = models.UUIDField(primary_key=True, unique=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_text = models.TextField()
    # video = models.FileField(blank=True)
    image = models.ImageField(blank=True, default='post_image.jpg', upload_to='post_images')
    created_at = models.DateTimeField(auto_now=timezone.now)

    def __str__(self) -> str:
        return super().__str__()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)

    def __str__(self) -> str:
        return super().__str__()

class Reaction(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    happy = models.PositiveIntegerField(default=0)
    love = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return super().__str__()

