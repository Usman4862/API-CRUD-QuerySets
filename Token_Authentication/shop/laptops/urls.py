from django.urls import path
from .views import * 


urlpatterns = [
    path('list/', LaptopView.as_view(), name='laptop-list'),
    path('list/<int:id>/', SingleLaptopView.as_view(), name='laptop-single'),

]
