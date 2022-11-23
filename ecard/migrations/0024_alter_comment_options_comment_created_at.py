# Generated by Django 4.1.3 on 2022-11-23 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecard', '0023_alter_card_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_at']},
        ),
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
