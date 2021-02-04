from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from django.views import View
import io
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class StudentDetails(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            data = Student.objects.get(id=id)
            serialize = StudentSerializer(instance=data)
            return JsonResponse(serialize.data)
        data = Student.objects.all()
        serialize = StudentSerializer(instance=data, many=True)
        return JsonResponse(serialize.data, safe=False)

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serialize = StudentSerializer(data=python_data)
        if serialize.is_valid():
            serialize.save()
            res = {'msg': 'Record Saved Successfully!!!'}
            return JsonResponse(res)
        res = serialize.errors
        return JsonResponse(res)

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        data = Student.objects.get(id=id)
        serialize = StudentSerializer(
            instance=data, data=python_data, partial=True)
        if serialize.is_valid():
            serialize.save()
            res = {'msg': 'Record Updated Successfully!!!'}
            return JsonResponse(res)
        res = serialize.errors
        return JsonResponse(res)

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        try:
            id = python_data.get('id')
            data = Student.objects.get(id=id)
            data.delete()
            res = {'msg': 'Record Deleted Successfully!!!'}
            return JsonResponse(res)
        except Exception:
            res = {
                'msg': 'DoesNotExistError :Requested Instance Object Not Found In Database.'}
            return JsonResponse(res)
