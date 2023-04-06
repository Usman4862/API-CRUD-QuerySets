from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.filters import OrderingFilter

class MovieView(generics.ListAPIView):
    queryset = SampleModel.objects.all()
    serializer_class = SampleModelSerializer
    filter_backends = [OrderingFilter]
    # ordering fields is used for the ordering for the specific fields
    ordering_fields = ['movie']