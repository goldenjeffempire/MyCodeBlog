from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='home'),  # List all posts
    path('create/', views.create_post, name='create_post'),  # Create a new post
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # Post details
]
