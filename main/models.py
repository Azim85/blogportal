from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files import File


class Post(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Yanglik egasi')
    title = models.CharField(max_length=50, verbose_name='Sarlavha')
    content = models.TextField(verbose_name='Kontent')
    post_added = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan sana')
    is_published = models.BooleanField(default=True, verbose_name='Saytga qo\'shilgan')
    image = models.ImageField(default='default.jpg', upload_to="post_pics", blank=True,
                              null=True,
                              width_field='img_w',
                              height_field='img_h',
                              verbose_name='Foydalanuvhci rasmi',)
    
    img_w = models.IntegerField(default=0)
    img_h = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Yanglik'
        verbose_name_plural = 'Yangliklar'
        
    def save(self, *args, **kwargs):
        if not self.image.closed:
            img = Image.open(self.image)
            img.thumbnail((500, 500), Image.ANTIALIAS)

            tmp = BytesIO()
            img.save(tmp, 'PNG')

            self.image = File(tmp, 'image.png')
        return super().save(*args, **kwargs)
    
