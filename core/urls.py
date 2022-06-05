from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import Dashboard, Register


app_name = 'core'

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', Register.as_view(), name='register'),
]