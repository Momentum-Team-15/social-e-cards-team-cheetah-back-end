from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(max_length=200, null=True, blank=True)
    


COLOR_CHOICES = {
('WHITE', 'WHITE'),
('RED', 'RED'),
('ORANGE', 'ORANGE'),
('YELLOW', 'YELLOW'),
('BLUE', 'BLUE'),
('GREEN', 'GREEN'),
('PURPLE', 'PURPLE'),
('BLACK', 'BLACK')
}

BORDER_STYLE_CHOICES = {
('SOLID', 'SOLID'),
('DOTTED', 'DOTTED'),
('DOUBLE', 'DOUBLE'),
('GROOVE', 'GROOVE')
}

FONT_FAMILY_CHOICES = {
('UBUNTO', 'UBUNTO'),
('ARIAL', 'ARIAL'),
('MERRIWEATHER', 'MERRIWEATHER'),
('RALEWAY', 'RALEWAY')
}

TEXT_ALIGNMENT_CHOICES = {
    ('LEFT', 'LEFT'),
    ('CENTER', 'CENTER'),
    ('RIGHT', 'RIGHT')
}


class Card(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    color = models.CharField(max_length=50, choices=COLOR_CHOICES, default='WHITE')
    border_style = models.CharField(max_length=50, choices=BORDER_STYLE_CHOICES, default='SOLID')
    border_color = models.CharField(max_length=50, choices=COLOR_CHOICES, default='BLACK')
    font_family = models.CharField(max_length=50, choices=FONT_FAMILY_CHOICES, default='UBUNTO')
    font_color = models.CharField(max_length=50, choices=COLOR_CHOICES, default='BLACK')
    text_alignment = models.CharField(max_length=50, choices=TEXT_ALIGNMENT_CHOICES, default='LEFT')
    outer_msg = models.CharField(max_length=200)
    inner_msg = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated_at']

class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.name

class Comment(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField(max_length=100)
    commentor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.comment

TAG_CHOICES = {
    ('BIRTHDAY', 'BIRTHDAY'),
    ('CHRISTMAS', 'CHRISTMAS'),
    ('WEDDING', 'WEDDING'),
    ('VALENTINES-DAY', 'VALENTINES-DAY'),
    ('THANK-YOU', 'THANK-YOU'),
    ('CONDOLENCES', 'CONDOLENCES')
}

class Tag(models.Model):
    type = models.CharField(max_length=50, choices=TAG_CHOICES, null=True, blank=True)
    tag = models.ManyToManyField(Card, related_name='tags')

    def __str__(self):
        return self.type

class Favorite(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, null=True, blank=True, related_name='favorites')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='favorites')
    created_at = models.DateTimeField(auto_now_add=True)