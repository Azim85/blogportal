# Generated by Django 3.1.4 on 2020-12-12 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20201212_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', height_field='img_h', null=True, upload_to='post_pics', verbose_name='Foydalanuvhci rasmi', width_field='img_w'),
        ),
    ]
