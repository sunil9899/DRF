from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    roll = serializers.IntegerField()
    section = serializers.CharField(max_length=100)

    def create(self, data):
        return Student.objects.create(**data)
