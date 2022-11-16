from rest_framework import serializers
from .models import User, Card, Tag, Comment, Friend, Favorite

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name','bio','username','email')

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id','title','user','border_style','border_color','font_family','font_color','text_alignment','outer_msg','inner_msg','created_at','updated_at','published')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'type','tag')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'card','comment','commentor')

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ('id', 'user',)


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('id', 'card','user','created_at')
