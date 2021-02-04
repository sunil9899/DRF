from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
