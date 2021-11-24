from django.contrib import admin
from django.urls.conf import include
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('app_lettings.urls'), name='lettings'),
    path('profiles/', include('app_profiles.urls'), name='profiles'),
    path('admin/', admin.site.urls),
]
