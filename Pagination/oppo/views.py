from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.authentication import SessionAuthentication
from .custompermissions import MyPermission
from .paginations import MyPagination


class OppoModelListView(generics.ListCreateAPIView):
    queryset = OppoModel.objects.all()
    serializer_class = OppoModelSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [MyPermission]
    pagination_class = MyPagination

class OppoModelAllView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OppoModel.objects.all()
    serializer_class = OppoModelSerializer
    lookup_field = 'id'
    authentication_classes = [SessionAuthentication]
    permission_classes = [MyPermission]


