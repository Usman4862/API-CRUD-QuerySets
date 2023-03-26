from django.contrib import admin
from django.urls import path
from sample.views import person_list, single_person, create_person, complete_update_person, partial_person, delete_person
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', person_list, name='id-function'),
    path('api/person/<int:id>/', single_person, name='single-id'),
    path('api/add/', create_person, name='create-person'),
    path('api/update/<int:id>/', complete_update_person, name='complete-person-update'),
    path('api/partial/update/<int:id>/', partial_person, name='partial-person'),
    path('api/delete/<int:id>/', delete_person, name='delete-person'),
    
]
