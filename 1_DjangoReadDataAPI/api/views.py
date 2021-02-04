from django.shortcuts import render, HttpResponse
from .serializers import StudentSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer
# Create your views here.


def home(request):
    return HttpResponse('<h3> This is Home Page </h3>')


def studentData(request):
    data = Student.objects.get(id=2)
    serialize = StudentSerializer(data)
    json_data = JSONRenderer().render(serialize.data)
    return HttpResponse(content=json_data, content_type='application/json')


def studentDataPK(request, pk):
    data = Student.objects.get(id=pk)
    serialize = StudentSerializer(data)
    json_data = JSONRenderer().render(serialize.data)
    return HttpResponse(content=json_data, content_type='application/json')


def studentDataAll(request):
    data = Student.objects.all()
    serialize = StudentSerializer(instance=data, many=True)
    json_data = JSONRenderer().render(serialize.data)
    return HttpResponse(content=json_data, content_type='application/json')
