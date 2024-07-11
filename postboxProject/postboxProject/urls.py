from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin12/', admin.site.urls),
    path('', include('posts.urls')),
]