from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Built-in Django auth views
    path('login/', views.custom_login, name='login'),  # Use custom login view
    path('logout/', views.logout_view, name='logout'),  # Use custom logout view
    
    # User registration and authentication
    path('signup/', views.signup, name='signup'),
    
    # Post management
    path('', views.post_list, name='home'),
    path('create/', views.create_post, name='create_post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('edit_post/<int:pk>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:pk>/', views.delete_post, name='delete_post'),
]
