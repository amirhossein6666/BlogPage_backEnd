from django.urls import path
from . import views
from .views import PostListView, PostDetailView , PostCreateView, PostUpdateView, PostDeleteView
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('post/<pk>', PostDetailView.as_view(), name='blog_detail'),
    path('post/<pk>/update', PostUpdateView.as_view(), name='blog-update'),
    path('post/<pk>/delete', PostDeleteView.as_view(), name='blog-delete'),
    path('posts/new/', PostCreateView.as_view(), name='blog-create'),
]
