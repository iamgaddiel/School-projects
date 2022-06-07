from django.urls import path

from .views import list_users, get_messages, send_message

app_name = 'chat'

urlpatterns = [
    path('list_users/', list_users, name='users'),
    path('get_messages/<int:friend_id>/', get_messages, name='get_messages'),
    path('send_message/<str:message>/<friend_id>/', send_message, name='send_messages'),
]