from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverview, name='apiOverview'),
    path('post-list/', views.ShowAll, name='post-list'),
    path('post-detail/<int:pk>/', views.ShowSingle, name='post-view'),
    path('post-create/', views.CreatePost, name='post-create'),
    path('post-update/<int:pk>/', views.UpdatePost, name='post-update'),
    path('post-delete/<int:pk>/', views.DeletePost, name='post-delete'),
    path('comment-list/', views.CommentAll, name='comment-list')
]
