from rest_framework import serializers
from .models import Student


def start_with_s(value):
    if value[0] != 's':
        raise serializers.ValidationError(
            'Name should be starts with S character only!!!')
    return value


class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[start_with_s])

    class Meta:
        model = Student
        # fields = ['id', 'name', 'roll', 'section']
        fields = '__all__'

    def validate_roll(self, value):
        if value > 200:
            raise serializers.ValidationError('Not Alloud! Seat Full!!!')
        return value

    def validate(self, data):
        nm = data.get('name')
        roll = data.get('roll')
        if nm.lower() == 'amit' and roll != 103:
            raise serializers.ValidationError(
                'Roll Number of Mr. Amit Should be 103')
        return data
