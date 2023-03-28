from django.shortcuts import render
from .models import *
from rest_framework import generics
from .serializers import *


class SweeperList(generics.ListAPIView):
    queryset = Sweeper.objects.all()
    serializer_class = SweeperSerializer


class SweeperPost(generics.CreateAPIView):
    queryset = Sweeper.objects.all()
    serializer_class = SweeperSerializer


class SweeperUpdate(generics.UpdateAPIView):
    queryset = Sweeper.objects.all()
    serializer_class = SweeperSerializer
    lookup_field = 'id'

class SweeperRetrieve(generics.RetrieveAPIView):
    queryset = Sweeper.objects.all()
    serializer_class = SweeperSerializer
    lookup_field = 'id'

class SweeperDelete(generics.DestroyAPIView):
    queryset = Sweeper.objects.all()
    serializer_class = SweeperSerializer
    lookup_field = 'id'