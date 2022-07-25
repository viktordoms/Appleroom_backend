from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .models import *
from .serializers import *


# Create your views here.
class CategoriesListView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
