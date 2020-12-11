from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files import File


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Foydalanuvhci')
    image = models.ImageField(default='default.jpg', upload_to="profile_pics", blank=True,
                              null=True,
                              width_field='img_w',
                              height_field='img_h',
                              verbose_name='Foydalanuvhci rasmi',
                              )

    img_w = models.IntegerField(default=0)
    img_h = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Profil'
        verbose_name_plural = 'Profillar'

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        if not self.image.closed:
            img = Image.open(self.image)
            img.thumbnail((500, 500), Image.ANTIALIAS)

            tmp = BytesIO()
            img.save(tmp, 'PNG')

            self.image = File(tmp, 'image.png')
        return super().save(*args, **kwargs)
