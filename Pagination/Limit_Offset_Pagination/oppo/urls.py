from django.urls import path
from .views import *


urlpatterns = [
    path('list/', OppoModelListView.as_view(), name='mobile-list'),
    path('list/<int:id>/', OppoModelAllView.as_view(), name='mobile-all'),
]
