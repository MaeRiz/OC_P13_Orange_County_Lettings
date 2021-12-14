from django.contrib import admin
from django.urls.conf import include
from django.urls import path

from . import views


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('app_lettings.urls'), name='lettings'),
    path('profiles/', include('app_profiles.urls'), name='profiles'),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
]
