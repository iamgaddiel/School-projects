from django.urls import path

from .views import (
    GroupView, 
    list_users, 
    get_messages, 
    send_group_message, 
    send_message, 
    GroupCreation, 
    get_group_messages
)

app_name = 'chat'

urlpatterns = [
    path('list_users/', list_users, name='users'),
    path('get_messages/<int:friend_id>/', get_messages, name='get_messages'),
    path('send_message/<str:message>/<friend_id>/', send_message, name='send_messages'),
    path('groups/', GroupView.as_view(), name='groups'),
    path('create-group/', GroupCreation.as_view(), name='create_group'),
    path('group_messages/<uuid:group_id>/', get_group_messages, name='group_messages'),
    path('send_group_message/<str:message>/<uuid:group_id>/', send_group_message, name='send_group_messages'),
]
