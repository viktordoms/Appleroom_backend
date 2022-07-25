from rest_framework import serializers
from .models import *


class NumberDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Number
        fields = "__all__"


class MainInfoSerializer(serializers.ModelSerializer):
    numbers = NumberDetailsSerializer(read_only=True, many=True)

    class Meta:
        model = City
        fields = '__all__'
