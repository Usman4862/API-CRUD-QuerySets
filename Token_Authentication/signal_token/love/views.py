from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class TestView(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    authentication_classes= [TokenAuthentication]
    permission_classes= [IsAuthenticatedOrReadOnly]

class SingleTestView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    lookup_field = 'id'
    authentication_classes= [TokenAuthentication]
    permission_classes= [IsAuthenticatedOrReadOnly]
