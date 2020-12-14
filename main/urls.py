from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import IndexView, SearchResaultView


app_name = 'main'

urlpatterns=[
        # path('', views.index, name='index'),
        path('', views.IndexView.as_view(), name="index"),
        path('create/', views.post_create, name='post-create'),
        path('edit/<int:post_id>/', views.post_edit, name='post-edit'),
        path('delete/<int:post_id>/', views.post_delete, name='post-delete'),
        path('more/<int:post_id>/', views.post_more, name='post-more'),
        path('all/<int:user_id>/', views.post_all, name='post-all'),
        path('search/', SearchResaultView.as_view(), name='search')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)