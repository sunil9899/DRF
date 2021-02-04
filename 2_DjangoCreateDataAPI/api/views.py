from django.shortcuts import render, HttpResponse
from .serializers import StudentSerializer
from .models import Student
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def createRecords(request):
    if request.method == 'POST':
        data = request.body
        stream = io.BytesIO(data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Record Created Successfully!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(content=json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(content=json_data, content_type='application/json')
    return HttpResponse('<h4> This is GET Method </h4>')
