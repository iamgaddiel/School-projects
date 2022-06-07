
from django.contrib import admin
from django.urls import include, path
from django.conf import settings

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('posts/', include('post.urls')),
    path('chat/', include('chat.urls')),
]

# urlpatterns += settings.