# Generated by Django 4.1.3 on 2022-11-16 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecard', '0010_alter_card_font_family_alter_card_text_alignment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='border_style',
            field=models.CharField(choices=[('DOUBLE', 'DOUBLE'), ('GROOVE', 'GROOVE'), ('SOLID', 'SOLID'), ('DOTTED', 'DOTTED')], default='SOLID', max_length=50),
        ),
        migrations.AlterField(
            model_name='card',
            name='font_family',
            field=models.CharField(choices=[('UBUNTO', 'UBUNTO'), ('ARIAL', 'ARIAL'), ('RALEWAY', 'RALEWAY'), ('MERRIWEATHER', 'MERRIWEATHER')], default='UBUNTO', max_length=50),
        ),
        migrations.AlterField(
            model_name='card',
            name='text_alignment',
            field=models.CharField(choices=[('CENTER', 'CENTER'), ('RIGHT', 'RIGHT'), ('LEFT', 'LEFT')], default='LEFT', max_length=50),
        ),
    ]
