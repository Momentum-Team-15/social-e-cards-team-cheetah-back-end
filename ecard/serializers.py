from rest_framework import serializers
from .models import User, Card, Tag, Comment, Friendship, Favorite

class UserSerializer(serializers.ModelSerializer):
    cards = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id','name','bio','username','email', 'avatar', 'cards', 'comments')

    def update(self, instance, validated_data):
        if "file" in self.initial_data:
            file = self.initial_data.get("file")
            instance.avatar.save(file.name, file, save=True)
            return instance
        # this call to super is to make sure that update still works for other fields
        return super().update(instance, validated_data)

class CommentSerializer(serializers.ModelSerializer):
    commentor = serializers.ReadOnlyField(source='commentor.username')

    class Meta:
        model = Comment
        fields = ('id', 'card','comment','commentor')

class CardSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Card
        fields = ('id','title','user','border_style','border_color','font_family','font_color','text_alignment','outer_msg','inner_msg','created_at','updated_at','published', 'comments', 'background_color')

class FriendUserSerializer(serializers.ModelSerializer):
    friend = serializers.SlugRelatedField(read_only=True, slug_field="username")

    class Meta:
        model = Friendship
        fields =('__all__')

class FriendSerializer(serializers.ModelSerializer):
    current_user = serializers.SlugRelatedField(read_only=True, slug_field="username")
    # friend = serializers.SlugRelatedField(read_only=True, slug_field="username")

    class Meta:
        model = Friendship
        fields = ('id', 'current_user','friend')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'type','tag')

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('id', 'card','user','created_at')


