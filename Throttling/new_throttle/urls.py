from django.urls import path
from .views import FakeRateThrottle, SingleRateThrottle

urlpatterns = [
    path('list/', FakeRateThrottle.as_view(), name='list-view'),
    path('list/<int:id>/', SingleRateThrottle.as_view(), name='single-view'),

]
