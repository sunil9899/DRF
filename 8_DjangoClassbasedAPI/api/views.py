from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class StudentAPI(APIView):
    def get(self, request, pk=None, format=None):
        if pk is not None:
            try:
                data = Student.objects.get(pk=pk)
                serialize = StudentSerializer(instance=data)
                return Response(serialize.data)
            except Exception:
                return Response({'Error': 'Record Not Available'}, status=status.HTTP_404_NOT_FOUND)
        data = Student.objects.all()
        serialize = StudentSerializer(instance=data, many=True)
        return Response(serialize.data)

    def post(self, request, format=None):
        data = request.data
        serialize = StudentSerializer(data=data)
        if serialize.is_valid():
            serialize.save()
            return Response({'Message': 'Record Created Successfully.'})
        return Response({'Error': 'Something Went Wrong!'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        try:
            ins = Student.objects.get(pk=pk)
            data = request.data
            serialize = StudentSerializer(instance=ins, data=data)
            if serialize.is_valid():
                serialize.save()
                return Response({'Message': 'Record Updated Successfully.'})
            return Response({'Error': 'Something Went Wrong.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({'Error': 'Object Instance Not Found'}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        try:
            ins = Student.objects.get(pk=pk)
            data = request.data
            serialize = StudentSerializer(
                instance=ins, data=data, partial=True)
            if serialize.is_valid():
                serialize.save()
                return Response({'Message': 'Record Updated Successfully.'})
            return Response({'Error': 'Something Went Wrong.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({'Error': 'Object Instance Not Found'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            ins = Student.objects.get(pk=pk)
            ins.delete()
            return Response({'Message': 'Record Deleted Successfully!!!'})
        except Exception:
            return Response({'Error': 'Object Instance Not Found'}, status=status.HTTP_400_BAD_REQUEST)
