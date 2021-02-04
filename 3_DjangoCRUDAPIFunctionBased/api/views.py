from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
def studentData(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        data = Student.objects.all()
        serializer = StudentSerializer(instance=data, many=True)
        id = python_data.get('id', None)
        if id is not None:
            data = Student.objects.get(id=id)
            serializer = StudentSerializer(instance=data)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(content=json_data, content_type='application/json')

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Record Saved Successfully!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = serializer.errors
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        data = Student.objects.get(id=id)
        serializer = StudentSerializer(
            instance=data, data=python_data, partial=True)  # if partial is not passed or set to False, then it will work like PATCH
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Record Updated Successfully!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = serializer.errors
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        try:
            data = Student.objects.get(id=id)
            data.delete()
            res = {'msg': 'Record Deleted Successfully!!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        except Exception:
            res = {'msg': 'Instance Object Not Found!!!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
