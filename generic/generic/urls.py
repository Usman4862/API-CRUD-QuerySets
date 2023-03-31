from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('example.urls')),
    path('auth/', include('rest_framework.urls')) # this line will add the login / logout functionality in the api by using session authentication
]
