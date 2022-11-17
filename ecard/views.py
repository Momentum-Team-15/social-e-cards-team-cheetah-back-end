from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import User, Card, Tag, Comment, Friend, Favorite
from .serializers import UserSerializer, CardSerializer, TagSerializer, CommentSerializer, FriendSerializer, FavoriteSerializer
from django.db.models import Q

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
        queryset = User.objects.filter(name=self.request.user.name)
        return queryset

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This Gets, allows to update, and delete a single user  
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CardListCreateView(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def get_queryset(self):
        return Card.objects.filter(Q(user=self.request.user) | Q(published=True))

    def perform_create(self, serializer):
        #this is to POST a new Card
        serializer.save(user=self.request.user)

class CardDetail(generics.RetrieveUpdateAPIView):
    """
    This Gets, allows to update, and delete a single card 
    """
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This Gets, allows to update, and delete a single card 
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class FriendListCreateView(generics.ListCreateAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

class FavoriteListCreateView(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer