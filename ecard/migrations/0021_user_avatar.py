# Generated by Django 4.1.3 on 2022-11-21 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecard', '0020_merge_0018_tag_unique_tag_0019_alter_friend_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='user_avatars'),
        ),
    ]
