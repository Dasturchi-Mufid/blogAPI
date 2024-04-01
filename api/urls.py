from django.urls import path
from . import views

urlpatterns = [
    path('',views.BlogPostListCreate.as_view(), name='blog-post-view-create'),
    path('<int:pk>/', views.BlogPostRetrieveUpdateDestroy.as_view(), name='update'),
    path('list', views.BlogPostList.as_view(), name='blog-post-list'),
]
