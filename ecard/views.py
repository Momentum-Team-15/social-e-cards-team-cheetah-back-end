from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Card, Tag, Comment, Friend, Favorite
from .serializers import CardSerializer, TagSerializer, CommentSerializer, FriendSerializer, FavoriteSerializer

# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'cards': reverse('card_list', request=request, format=format),
    })

class CardListCreateView(generics.ListCreateAPIView):
    queryset = Card.objects.objects.all()
    serializer_class = CardSerializer

class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.objects.all()
    serializer_class = TagSerializer

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.objects.all()
    serializer_class = CommentSerializer

class FriendListCreateView(generics.ListCreateAPIView):
    queryset = Friend.objects.objects.all()
    serializer_class = FriendSerializer

class FavoriteListCreateView(generics.ListCreateAPIView):
    queryset = Favorite.objects.objects.all()
    serializer_class = FavoriteSerializer