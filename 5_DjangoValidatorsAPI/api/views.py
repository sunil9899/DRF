from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse


@method_decorator(csrf_exempt, name='dispatch')
class StudentData(View):
    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serialize = StudentSerializer(data=python_data)
        if serialize.is_valid():
            serialize.save()
            res = {'msg': 'Data Saved Successfully!!!'}
            # json_data = JSONRenderer().render(res)
            return JsonResponse(res, safe=False)
        json_data = serialize.errors
        return JsonResponse(json_data)
