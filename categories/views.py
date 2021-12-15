from rest_framework import viewsets

from .models import Category

from .serializers import CategorySerializers


class CategoryAPIView(viewsets.ModelViewSet):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()