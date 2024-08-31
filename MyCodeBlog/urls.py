from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('VoiceHub.urls')),  # Ensure VoiceHub URLs are included
]
