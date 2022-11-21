from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import User, Card, Tag, Comment, Friend, Favorite
from .serializers import UserSerializer, CardSerializer, TagSerializer, CommentSerializer, FriendSerializer, FavoriteSerializer
from django.db.models import Q
from django.contrib.postgres.search import SearchVector,SearchQuery,SearchRank
from itertools import chain
from drf_multiple_model.views import ObjectMultipleModelAPIView

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
        queryset = User.objects.filter(username=self.request.user)
        return queryset

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This Gets, allows to update, and delete a single user  
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserSearchList(generics.ListAPIView):
    model = User
    context_object_name = "quotes"
    serializer_class= UserSerializer

    def get_queryset(self):
        query = self.request.GET.get("q")
        return User.objects.annotate(search=SearchVector("username","name")).filter(
            search=query
        )

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

class CardSearchList(ObjectMultipleModelAPIView):

    def get_querylist(self):
        request = self.request
        query = request.GET.get('q', None)

        if query:
            queryset = [
                {'queryset':Card.objects.filter(title=query),'serializer_class':CardSerializer},
                {'queryset':Tag.objects.filter(type=query),'serializer_class':TagSerializer},
                {'queryset':User.objects.filter(Q(username=query) | Q(name=query)),'serializer_class':UserSerializer},
            ]

            return queryset

class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
class TagDetail(generics.RetrieveUpdateAPIView):
    """
    This Gets, allows to update, and delete a single card 
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

# ---------------------------------------------------- ray starts here
class CommentListCreateView(generics.ListCreateAPIView): 
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

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

    #associating the user who is creating this Friend
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FriendDetailView(generics.RetrieveDestroyAPIView):
    #this gets and deletes a single Friend 
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

class FavoriteListCreateView(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    #filter favorites by the logged in user
    def get_queryset(self):
        return self.request.user.favorites.all()

    #associate the user who is creating this favorite
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FavoriteDetailView(generics.RetrieveDestroyAPIView):
    #this gets and deletes a single Favorite 
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
