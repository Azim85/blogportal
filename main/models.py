from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Yanglik egasi')
    title = models.CharField(max_length=50, verbose_name='Sarlavha')
    content = models.TextField(verbose_name='Kontent')
    post_added = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan sana')
    is_published = models.BooleanField(default=True, verbose_name='Saytga qo\'shilgan')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Yanglik'
        verbose_name_plural = 'Yangliklar'
