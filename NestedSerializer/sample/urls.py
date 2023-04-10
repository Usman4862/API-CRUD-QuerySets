from django.contrib import admin
from django.urls import path, include
from api.views import SingerViewSet, SongViewSet
from rest_framework.routers import DefaultRouter


# Router Object

router = DefaultRouter()


# Register

router.register('singer', SingerViewSet, basename='singer')
router.register('song', SongViewSet, basename='song')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth', include('rest_framework.urls')),
    path('', include(router.urls)),
]
