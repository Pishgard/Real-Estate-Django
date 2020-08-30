from django.urls import path
from .views import BlogView, BlogPost

urlpatterns = [
    path('', BlogView, name='blog'),
    path('<int:id>', BlogPost, name='post_blog'),
]
