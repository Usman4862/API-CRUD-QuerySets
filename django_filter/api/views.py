from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

class MovieView(generics.ListAPIView):
    queryset = SampleModel.objects.all()
    serializer_class = SampleModelSerializer
    # filter backends is used for the django filter backend
    filter_backends = [DjangoFilterBackend  ]
    # use your desired fields for filtering 
    filterset_fields = [
        'id',
        'movie',
        'series',
        'phone_number',
        
    ]