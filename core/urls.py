from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import Dashboard, ProfileDetail, Register, profile_update

from post.views import PostFeed


app_name = 'core'

urlpatterns = [
    path('', PostFeed.as_view(), name='dashboard'),
    # path('', Dashboard.as_view(), name='dashboard'),
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('profile/', ProfileDetail.as_view(), name='profile'),
    path('profile/update/', profile_update, name='profile_update'),
]