from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .models import BlogPost, UserProfile, User
from .views import search, blog_post_create  # Add the blog_post_create import here
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('delete_image/<int:image_id>/', views.delete_image, name='delete_image'),
    path('display_images/', views.display_images, name='display_images'),
    path('search_suggestions/', views.search_suggestions, name='search_suggestions'),
    path('', views.BlogPostListView.as_view(), name='blog_post_list'),
    path('user_profiles/<int:pk>/', views.UserProfileDetailView.as_view(), name='user_profile_detail'),
    path('register/', views.register, name='register'),
    path('user_profiles/', views.user_profile_list, name='user_profile_list'),
    path('user_profiles/create/', views.UserProfileCreateView.as_view(), name='user_profile_create'),
    path('user_profiles/<int:pk>/update/', views.UserProfileUpdateView.as_view(), name='user_profile_update'),
    path('user_profiles/<int:pk>/delete/', views.UserProfileDeleteView.as_view(), name='user_profile_delete'),
    path('blog_post/<int:pk>/', views.BlogPostDetailView.as_view(), name='blog_post_detail'),
    path('blog_post/create/', blog_post_create, name='blog_post_create'),  # Update this line
    path('blog_post/<int:pk>/update/', views.BlogPostUpdateView.as_view(), name='blog_post_update'),
    path('blog_post/<int:pk>/delete/', views.BlogPostDeleteView.as_view(), name='blog_post_delete'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('search/', search, name='search'),
    path('upload/', views.upload_file, name='upload_file'),
    path('upload/success/', views.upload_success, name='upload_success'),
    path('change-password/', views.change_password, name='change_password'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

