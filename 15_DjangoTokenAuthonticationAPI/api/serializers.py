from rest_framework import serializers
from .models import Student


def isLower(value):
    if value[0].islower():
        raise serializers.ValidationError(
            'First Character Of Name Should Be Upper Case')
    return value


class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[isLower])

    class Meta:
        model = Student
        fields = "__all__"
