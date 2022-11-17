from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import User, Card, Tag, Comment, Friend, Favorite
from .serializers import UserSerializer, CardSerializer, TagSerializer, CommentSerializer, FriendSerializer, FavoriteSerializer

# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'cards': reverse('card_list', request=request, format=format),
    })

class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.filter(user=self.request.user)
        return queryset

class CardListCreateView(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

# ---------------------------------------------------- ray starts here
class CommentListCreateView(generics.ListCreateAPIView): 
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    #filter Comments by the logged in user
    def get_queryset(self):
        return self.request.user.comments.all()

    #associating the user who is creating this Comment
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    #this gets, allows to update, and delete a single Comment 
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class FriendListCreateView(generics.ListCreateAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

    def get_queryset(self):
        return self.request.user.friends.all()

    #associating the user who is creating this Friend
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FriendDetailView(generics.RetrieveDestroyAPIView):
    #this gets and deletes a single Friend 
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

class FavoriteListCreateView(generics.ListCreateAPIView):
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        return self.request.user.favorites.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FavoriteDetailView(generics.RetrieveUpdateDestroyAPIView):
    #this gets, allows to update, and delete a single Favorite 
    queryset = Favorite.objects.all
    serializer_class = FavoriteSerializer
