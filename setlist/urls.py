from django.contrib import admin
from django.urls import path
from .views import get_setlists, add, edit, delete

urlpatterns = [
    # path('admin/', admin.site.urls),
    # when want to add summernote to a field, watch 5.20 creating admin pannel
    # path('summernote/', include('django_summernote.urls')),
    # path('accounts/', include('allauth.urls')),
    # path('/', include('home.urls')),
    path('', get_setlists, name='setlist'),
    path('add/', add, name='add_setlist'),
    path('edit/<str:pk>/', edit, name='edit_setlist'),
    path('delete/<str:pk>/', delete, name='delete_setlist'),
]