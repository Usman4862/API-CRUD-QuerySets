from django.contrib import admin
from django.urls import path, include
from laptops.auth import CustomTokenAuth


urlpatterns = [
    path('admin/', admin.site.urls),
    path('laptop/', include('laptops.urls')),
    path('auth', include('rest_framework.urls')),
    path('get-token/', CustomTokenAuth.as_view()),
]
