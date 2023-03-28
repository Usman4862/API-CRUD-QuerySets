from django.urls import path
from .views import *


urlpatterns = [
    path('', SweeperList.as_view(), name='sweeper-list'),
    path('create/', SweeperPost.as_view(), name='sweeper-post'),
    path('update/<id>/', SweeperUpdate.as_view(), name='sweeper-update'),
    path('retrieve/<id>/', SweeperRetrieve.as_view(), name='sweeper-retrieve'),
    path('delete/<id>/', SweeperDelete.as_view(), name='sweeper-delete'),
]
