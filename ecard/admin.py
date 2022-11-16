from django.contrib import admin
from .models import User, Card, Friend, Favorite, Tag, Comment

# Register your models here.

admin.site.register(User)
admin.site.register(Card)
admin.site.register(Friend)
admin.site.register(Favorite)
admin.site.register(Tag)
admin.site.register(Comment)