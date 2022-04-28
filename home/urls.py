from django.contrib import admin
from django.urls import path, include
from home.views import home

urlpatterns = [
    # path('admin/', admin.site.urls),
    # when want to add summernote to a field, watch 5.20 creating admin pannel
    # path('summernote/', include('django_summernote.urls')),
    # path('accounts/', include('allauth.urls')),
    # path('/', include('home.urls')),
    path('', home, name='home')
]