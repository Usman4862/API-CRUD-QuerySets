from django.contrib import admin
from django.urls import path
from api.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', MovieView.as_view(), name='id-function'),
    
]
