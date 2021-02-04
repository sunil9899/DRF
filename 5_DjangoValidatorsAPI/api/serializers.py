from rest_framework import serializers
from .models import Student


def start_with_s(value):
    if value[0].lower() != 's':
        raise serializers.ValidationError('Name Should Be starts With S only')
    return value


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[start_with_s])
    roll = serializers.IntegerField()
    section = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    # field level validators
    def validate_roll(self, value):
        if value > 200:
            raise serializers.ValidationError('Seat Full')
        return value

    # object level validators
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'amit' and ct.lower() != 'lko':
            raise serializers.ValidationError(
                'City Name should be Lucknow Only')
        return data
