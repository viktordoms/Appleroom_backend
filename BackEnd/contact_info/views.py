from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .models import City
from .serializers import MainInfoSerializer


class CityInfoView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = City.objects.filter
    serializer_class = MainInfoSerializer
