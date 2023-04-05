from django.urls import path
from .views import *


urlpatterns = [
    path('list/', TestListView.as_view(), name='api-list'),
    path('list/<int:id>/', TestSingleView.as_view(), name='api-single'),
]
