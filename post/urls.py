from django.urls import path

from .views import PersonalPosts, PostFeed, CreatePost, delete_post

app_name = 'post'

urlpatterns = [
    path('feed/', PostFeed.as_view(), name='feed'),
    path('create/', CreatePost.as_view(), name='create_post'),
    path('my_post/', PersonalPosts.as_view(), name='personal_post'),
    path('delete/<uuid:id>/', delete_post, name='delete_post'),
]