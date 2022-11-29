from django.contrib import admin
from .models import User, Card, Friendship, Favorite, Tag, Comment
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Card)
admin.site.register(Friendship)
admin.site.register(Favorite)
admin.site.register(Tag)
admin.site.register(Comment)