# Generated by Django 4.1.3 on 2022-11-16 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecard', '0013_alter_card_border_style_alter_card_font_family_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='border_color',
            field=models.CharField(choices=[('ORANGE', 'ORANGE'), ('BLACK', 'BLACK'), ('PURPLE', 'PURPLE'), ('WHITE', 'WHITE'), ('RED', 'RED'), ('YELLOW', 'YELLOW'), ('GREEN', 'GREEN'), ('BLUE', 'BLUE')], default='BLACK', max_length=50),
        ),
        migrations.AlterField(
            model_name='card',
            name='border_style',
            field=models.CharField(choices=[('DOTTED', 'DOTTED'), ('DOUBLE', 'DOUBLE'), ('GROOVE', 'GROOVE'), ('SOLID', 'SOLID')], max_length=50),
        ),
        migrations.AlterField(
            model_name='card',
            name='color',
            field=models.CharField(choices=[('ORANGE', 'ORANGE'), ('BLACK', 'BLACK'), ('PURPLE', 'PURPLE'), ('WHITE', 'WHITE'), ('RED', 'RED'), ('YELLOW', 'YELLOW'), ('GREEN', 'GREEN'), ('BLUE', 'BLUE')], default='WHITE', max_length=50),
        ),
        migrations.AlterField(
            model_name='card',
            name='font_color',
            field=models.CharField(choices=[('ORANGE', 'ORANGE'), ('BLACK', 'BLACK'), ('PURPLE', 'PURPLE'), ('WHITE', 'WHITE'), ('RED', 'RED'), ('YELLOW', 'YELLOW'), ('GREEN', 'GREEN'), ('BLUE', 'BLUE')], default='BLACK', max_length=50),
        ),
        migrations.AlterField(
            model_name='card',
            name='font_family',
            field=models.CharField(choices=[('RALEWAY', 'RALEWAY'), ('ARIAL', 'ARIAL'), ('MERRIWEATHER', 'MERRIWEATHER'), ('UBUNTO', 'UBUNTO')], max_length=50),
        ),
        migrations.AlterField(
            model_name='card',
            name='text_alignment',
            field=models.CharField(choices=[('RIGHT', 'RIGHT'), ('CENTER', 'CENTER'), ('LEFT', 'LEFT')], max_length=50),
        ),
        migrations.AlterField(
            model_name='tag',
            name='type',
            field=models.CharField(blank=True, choices=[('WEDDING', 'WEDDING'), ('CHRISTMAS', 'CHRISTMAS'), ('THANK-YOU', 'THANK-YOU'), ('VALENTINES-DAY', 'VALENTINES-DAY'), ('CONDOLENCES', 'CONDOLENCES'), ('BIRTHDAY', 'BIRTHDAY')], max_length=50, null=True),
        ),
    ]
