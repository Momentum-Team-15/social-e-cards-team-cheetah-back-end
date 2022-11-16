# Generated by Django 4.1.3 on 2022-11-16 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecard', '0005_alter_card_border_color_alter_card_border_style_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='border_color',
            field=models.CharField(choices=[('ORANGE', 'ORANGE'), ('BLUE', 'BLUE'), ('YELLOW', 'YELLOW'), ('WHITE', 'WHITE'), ('BLACK', 'BLACK'), ('GREEN', 'GREEN'), ('PURPLE', 'PURPLE'), ('RED', 'RED')], default='BLACK', max_length=50),
        ),
        migrations.AlterField(
            model_name='card',
            name='border_style',
            field=models.CharField(choices=[('DOTTED', 'DOTTED'), ('DOUBLE', 'DOUBLE'), ('SOLID', 'SOLID'), ('GROOVE', 'GROOVE')], default='SOLID', max_length=50),
        ),
        migrations.AlterField(
            model_name='card',
            name='color',
            field=models.CharField(choices=[('ORANGE', 'ORANGE'), ('BLUE', 'BLUE'), ('YELLOW', 'YELLOW'), ('WHITE', 'WHITE'), ('BLACK', 'BLACK'), ('GREEN', 'GREEN'), ('PURPLE', 'PURPLE'), ('RED', 'RED')], default='WHITE', max_length=50),
        ),
        migrations.AlterField(
            model_name='card',
            name='font_color',
            field=models.CharField(choices=[('ORANGE', 'ORANGE'), ('BLUE', 'BLUE'), ('YELLOW', 'YELLOW'), ('WHITE', 'WHITE'), ('BLACK', 'BLACK'), ('GREEN', 'GREEN'), ('PURPLE', 'PURPLE'), ('RED', 'RED')], default='BLACK', max_length=50),
        ),
        migrations.AlterField(
            model_name='card',
            name='font_family',
            field=models.CharField(choices=[('RALEWAY', 'RALEWAY'), ('UBUNTO', 'UBUNTO'), ('MERRIWEATHER', 'MERRIWEATHER'), ('ARIAL', 'ARIAL')], default='UBUNTO', max_length=50),
        ),
        migrations.AlterField(
            model_name='card',
            name='text_alignment',
            field=models.CharField(choices=[('LEFT', 'LEFT'), ('RIGHT', 'RIGHT'), ('CENTER', 'CENTER')], default='LEFT', max_length=50),
        ),
        migrations.AlterField(
            model_name='tag',
            name='type',
            field=models.CharField(blank=True, choices=[('CONDOLENCES', 'CONDOLENCES'), ('BIRTHDAY', 'BIRTHDAY'), ('CHRISTMAS', 'CHRISTMAS'), ('WEDDING', 'WEDDING'), ('THANK-YOU', 'THANK-YOU'), ('VALENTINES-DAY', 'VALENTINES-DAY')], max_length=50, null=True),
        ),
    ]