from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'main'

urlpatterns=[
        path('', views.index, name='index'),
        path('create/', views.post_create, name='post-create'),
        path('edit/<int:post_id>/', views.post_edit, name='post-edit'),
        path('delete/<int:post_id>/', views.post_delete, name='post-delete')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)