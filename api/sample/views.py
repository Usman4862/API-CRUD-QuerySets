from .models import SampleModel
from .serializers import SampleModelSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def person_list(request):
    person = SampleModel.objects.all()
    serializer = SampleModelSerializer(person, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def single_person(request, id):
    person = SampleModel.objects.get(id=id)
    serialzer = SampleModelSerializer(person)
    return Response(serialzer.data, status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
def create_person(request):
    data = request.data
    serializer = SampleModelSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def complete_update_person(request, id):
    data = request.data
    person = SampleModel.objects.get(id=id)
    serializer = SampleModelSerializer(person, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.data, status=status.HTTP_304_NOT_MODIFIED)

@api_view(['PATCH'])
def partial_person(request, id):
    data = request.data
    person = SampleModel.objects.get(id=id)
    serializer = SampleModelSerializer(person, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.data, status=status.HTTP_304_NOT_MODIFIED)

@api_view(['DELETE'])
def delete_person(request, id):
    person = SampleModel.objects.get(id=id)
    person.delete()
    return Response("Person Deleted", status=status.HTTP_200_OK)



