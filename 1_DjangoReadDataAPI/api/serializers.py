from rest_framework import serializers


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    roll = serializers.IntegerField()
    section = serializers.CharField(max_length=50)
