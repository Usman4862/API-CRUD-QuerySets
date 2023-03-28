from .models import *
from .serializers import ExampleModelSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class ExampleListView(APIView):
    def get(self, request):
        details = ExampleModel.objects.all()
        serializer = ExampleModelSerializer(details, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serialzer = ExampleModelSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExampleDetailView(APIView):
    def get_object(self, id):
        try:
            details = ExampleModel.objects.get(id=id)
            return details
        except:
            raise Http404
    
    def get(self, request, id, format=None):
        details = self.get_object(id)
        serializer = ExampleModelSerializer(details)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        details = self.get_object(id)
        serializer = ExampleModelSerializer(details)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        try:
            details = self.get_object(id)
            details.delete()
            return Response({'Messege': 'Deleted'}, status=status.HTTP_200_OK)
        except:
            return Response({'Messege': 'Not Deleted'}, status=status.HTTP_400_BAD_REQUEST)



    


    
