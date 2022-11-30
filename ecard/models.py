from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(max_length=200, null=True, blank=True)
    avatar = models.ImageField(upload_to="user_avatars", blank=True, null=True)

    
class Card(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='cards')
    background_color = models.CharField(max_length=50)
    border_style = models.CharField(max_length=50)
    border_color = models.CharField(max_length=50)
    font_family = models.CharField(max_length=50)
    font_color = models.CharField(max_length=50)
    text_alignment = models.CharField(max_length=50)
    outer_msg = models.CharField(max_length=200)
    inner_msg = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Friendship(models.Model):
    current_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='curent_users')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendships')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['current_user', 'friend'], name='unique_friendship')
        ]

    def __str__(self):
        return f"{self.current_user} is friends with {self.friend}"

class Comment(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField(max_length=100)
    commentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ['created_at']

class Tag(models.Model):
    type = models.CharField(max_length=50, null=True, blank=True)
    tag = models.ManyToManyField(Card, related_name='tags')

    def __str__(self):
        return self.type
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['type',], name='Unique_tag')
        ]

class Favorite(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='favorites')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    created_at = models.DateTimeField(auto_now_add=True)