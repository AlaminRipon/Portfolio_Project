from django.urls import path
from . import views

urlpatterns = [
  path('blogs/', views.blogs, name='blogs'),
  path('blogs/<int:blog_id>/', views.detail, name='detail'),
]