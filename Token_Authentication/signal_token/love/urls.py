from django.urls import path
from .views import *


urlpatterns = [
    path('list/', TestView.as_view()),
    path('list/<int:id>/', SingleTestView.as_view()),
]
