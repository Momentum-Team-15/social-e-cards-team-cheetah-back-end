# Generated by Django 4.1.3 on 2022-11-16 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecard', '0014_alter_card_border_color_alter_card_border_style_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={},
        ),
        migrations.AlterField(
            model_name='card',
            name='border_color',
            field=models.CharField(choices=[('ORANGE', 'ORANGE'), ('GREEN', 'GREEN'), ('RED', 'RED'), ('PURPLE', 'PURPLE'), ('YELLOW', 'YELLOW'), ('WHITE', 'WHITE'), ('BLUE', 'BLUE'), ('BLACK', 'BLACK')], default='BLACK', max_length=50),
        ),
        migrations.AlterField(
            model_name='card',
            name='border_style',
            field=models.CharField(choices=[('GROOVE', 'GROOVE'), ('DOUBLE', 'DOUBLE'), ('SOLID', 'SOLID'), ('DOTTED', 'DOTTED')], max_length=50),
        ),
        migrations.AlterField(
            model_name='card',
            name='color',
            field=models.CharField(choices=[('ORANGE', 'ORANGE'), ('GREEN', 'GREEN'), ('RED', 'RED'), ('PURPLE', 'PURPLE'), ('YELLOW', 'YELLOW'), ('WHITE', 'WHITE'), ('BLUE', 'BLUE'), ('BLACK', 'BLACK')], default='WHITE', max_length=50),
        ),
        migrations.AlterField(
            model_name='card',
            name='font_color',
            field=models.CharField(choices=[('ORANGE', 'ORANGE'), ('GREEN', 'GREEN'), ('RED', 'RED'), ('PURPLE', 'PURPLE'), ('YELLOW', 'YELLOW'), ('WHITE', 'WHITE'), ('BLUE', 'BLUE'), ('BLACK', 'BLACK')], default='BLACK', max_length=50),
        ),
        migrations.AlterField(
            model_name='card',
            name='font_family',
            field=models.CharField(choices=[('ARIAL', 'ARIAL'), ('MERRIWEATHER', 'MERRIWEATHER'), ('UBUNTO', 'UBUNTO'), ('RALEWAY', 'RALEWAY')], max_length=50),
        ),
        migrations.AlterField(
            model_name='card',
            name='text_alignment',
            field=models.CharField(choices=[('LEFT', 'LEFT'), ('RIGHT', 'RIGHT'), ('CENTER', 'CENTER')], max_length=50),
        ),
        migrations.AlterField(
            model_name='tag',
            name='type',
            field=models.CharField(blank=True, choices=[('WEDDING', 'WEDDING'), ('CONDOLENCES', 'CONDOLENCES'), ('VALENTINES-DAY', 'VALENTINES-DAY'), ('BIRTHDAY', 'BIRTHDAY'), ('THANK-YOU', 'THANK-YOU'), ('CHRISTMAS', 'CHRISTMAS')], max_length=50, null=True),
        ),
    ]