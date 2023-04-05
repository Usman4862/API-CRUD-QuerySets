from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('api/', include('jwt_api.urls')),
    path('access-token/', TokenObtainPairView.as_view(), name='access-token'),
    path('refresh-token/', TokenRefreshView.as_view(), name='refresh-token'),
    path('verify-token/', TokenVerifyView.as_view(), name='verify-token'),
]
