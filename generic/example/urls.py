from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('list/', ExampleListView.as_view(), name='list'),
    path('list/<int:id>/', ExampleDetailView.as_view(), name='list-single'),
]

urlpatterns=format_suffix_patterns(urlpatterns)