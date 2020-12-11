from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'main'

urlpatterns=[
        path('', views.index, name='index'),
        path('create/', views.post_create, name='post-create')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)