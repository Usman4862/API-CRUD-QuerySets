from django.shortcuts import render
from .serializers import LaptopSerializer
from .models import Laptop
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class LaptopView(generics.ListCreateAPIView):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class SingleLaptopView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
