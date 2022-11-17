from django.urls import path, include
from . import views

urlpatterns = [

path('profile/', views.UserView.as_view(), name='user-profile'),
path('cards/', views.CardListCreateView.as_view(), name='card-list'),
path('tags/', views.TagListCreateView.as_view(), name='tag-list'),
path('comments/', views.CommentListCreateView.as_view(), name='comment-list'),
path('comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail'),
path('friends/', views.FriendListCreateView.as_view(), name='friend-list'),
path('friends/<int:pk>/', views.FriendDetailView.as_view(), name='friend-detail'),
path('favorites/', views.FavoriteListCreateView.as_view(), name='favorite-list'),
path('favorites/<int:pk>/', views.FavoriteDetailView.as_view(), name='favorite-detail'),

]

