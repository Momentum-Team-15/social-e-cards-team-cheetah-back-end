from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import User, Card, Tag, Comment, Friendship, Favorite
from .serializers import UserSerializer, CardSerializer, TagSerializer, FriendUserSerializer, CommentSerializer, FriendSerializer, FavoriteSerializer
from django.db.models import Q
from django.contrib.postgres.search import SearchVector,SearchQuery,SearchRank
from itertools import chain
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework import parsers
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.db import IntegrityError
# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'cards': reverse('card_list', request=request, format=format),
    })

class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = User.objects.filter(username=self.request.user)
        return queryset

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This Gets, allows to update, and delete a single user  
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class UserSearchList(generics.ListAPIView):
    model = User
    context_object_name = "quotes"
    serializer_class= UserSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        query = self.request.GET.get("q")
        return User.objects.annotate(search=SearchVector("username","name")).filter(
            search=query
        )

class CardUser(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Card.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        #this is to POST a new Card
        serializer.save(user=self.request.user)

class CardListCreateView(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Card.objects.filter(Q(user=self.request.user) | Q(published=True))

    def perform_create(self, serializer):
        #this is to POST a new Card
        serializer.save(user=self.request.user)

class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This Gets, allows to update, and delete a single card 
    """
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]

class CardSearchList(ObjectMultipleModelAPIView):
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
    
class TagDetail(generics.RetrieveUpdateAPIView):
    """
    This Gets, allows to update, and delete a single Tag 
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]

# ---------------------------------------------------- ray starts here
class CommentListCreateView(generics.ListCreateAPIView): 
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    #associating the user who is creating this Comment
    def perform_create(self, serializer):
        serializer.save(commentor=self.request.user)

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    #this gets, allows to update, and delete a single Comment 
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class FriendListCreateView(generics.ListCreateAPIView):
    queryset = Friendship.objects.all()
    serializer_class = FriendSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Friendship.objects.filter(current_user=self.request.user.id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(current_user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return FriendUserSerializer
        return self.serializer_class

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            error_data = {
                "error": "You are already friends with this user."
            }
            return Response(error_data, status=status.HTTP_400_BAD_REQUEST)

class FriendDetailView(generics.RetrieveDestroyAPIView):
    #this gets and deletes a single Friend
    queryset = Friendship.objects.all()
    serializer_class = FriendSerializer
    permission_classes = [IsAuthenticated]


class FavoriteListCreateView(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticated]

class UserAvatarView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = [parsers.FileUploadParser]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        #return User.objects.first()
        return self.request.user
