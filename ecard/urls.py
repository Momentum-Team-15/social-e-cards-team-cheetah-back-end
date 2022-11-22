from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [

path('profile/', views.UserView.as_view(), name='user-profile'),
path('profile/me/',views.UserDetail.as_view(), name='user-detail'),
path('profile/search/', views.UserSearchList.as_view(), name="user-search"),
path('cards/', views.CardListCreateView.as_view(), name='card-list'),
path('cards/<int:pk>/',views.CardDetail.as_view(),name='card-detail'),
path('search-all/', views.CardSearchList.as_view(), name="card-search"),
path('tags/', views.TagListCreateView.as_view(), name='tag-list'),
path('tags/<int:pk>/',views.TagDetail.as_view(),name='tag-detail'),
path('comments/', views.CommentListCreateView.as_view(), name='comment-list'),
path('comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail'),
path('friends/', views.FriendListCreateView.as_view(), name='friend-list'),
path('friends/<int:pk>/', views.FriendDetailView.as_view(), name='friend-detail'),
path('favorites/', views.FavoriteListCreateView.as_view(), name='favorite-list'),
path('favorites/<int:pk>/', views.FavoriteDetailView.as_view(), name='favorite-detail'),
# No djsoer, but keeping this path since it'll be this eventually
path("auth/users/me/avatar/", views.UserAvatarView.as_view(), name='user_avatar'),
path('cards/user/', views.CardUser.as_view(),name='cards-user'),

]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)