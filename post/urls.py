from django.urls import path

from .views import PostFeed, CreatePost

app_name = 'post'

urlpatterns = [
    path('feed/', PostFeed.as_view(), name='feed'),
    path('create/', CreatePost.as_view(), name='create_post'),
]