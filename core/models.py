from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image  = models.ImageField(upload_to='profile_images', default='profile_image.jpg')

    def __str__(self) -> str:
        return f"{self.user.username}'s profile"
