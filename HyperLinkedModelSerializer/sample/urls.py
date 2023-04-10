from django.contrib import admin
from django.urls import path, include
from example.views import SampleViewSet
from rest_framework.routers import DefaultRouter


# creating obj
router = DefaultRouter()

router.register('example', SampleViewSet, basename='example')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
