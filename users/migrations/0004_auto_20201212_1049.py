# Generated by Django 3.1.4 on 2020-12-12 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201211_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='guest.jpg', height_field='img_h', null=True, upload_to='profile_pics', verbose_name='Foydalanuvhci rasmi', width_field='img_w'),
        ),
    ]
