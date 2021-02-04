from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        data = Student.objects.all()
        serialize = StudentSerializer(data, many=True)
        return Response(serialize.data)

    def create(self, request):
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Success!': 'Record Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        data = Student.objects.get(pk=pk)
        serializer = StudentSerializer(instance=data)
        return Response(serializer.data)

    def update(self, request, pk=None):
        ins = Student.objects.get(pk=pk)
        data = request.data
        serialize = StudentSerializer(instance=ins, data=data)
        if serialize.is_valid():
            serialize.save()
            return Response({'Success!': 'Record Updated Successfully.'}, status=status.HTTP_201_CREATED)
        return Response({'Error': 'Wrong Entry.'})

    def partial_update(self, request, pk=None):
        ins = Student.objects.get(pk=pk)
        data = request.data
        serialize = StudentSerializer(instance=ins, data=data, partial=True)
        if serialize.is_valid():
            serialize.save()
            return Response({'Success!': 'Record Updated Successfully.'}, status=status.HTTP_201_CREATED)
        return Response({'Error': 'Wrong Entry.'})

    def destroy(self, request, pk=None):
        data = Student.objects.get(pk=pk)
        data.delete()
        return Response({'Message': 'Record Deleted Successfully.'})
