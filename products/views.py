from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination

from rest_framework.response import Response
from rest_framework import status

from django.db.models import Q

from .models import Product
from .permissions import IsOwnerOrStaffOrReadOnly

from .serializers import ProductSerializers


class ProductPagination(PageNumberPagination):
    page_size = 10


class ProductAPIView(viewsets.ModelViewSet):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    permission_classes = [IsOwnerOrStaffOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=False, methods=['get'])
    def search(self, request, pk=None):
        t = request.query_params.get('t')
        queryset = self.queryset.filter(
            Q(name__icontains=t) |
            Q(description__icontains=t)
        )
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def filter_price(self, request, pk=None):
        p1 = request.query_params.get('p1')
        p2 = request.query_params.get('p2')
        queryset = self.queryset.filter(
            Q(price__gte=p1) &
            Q(price__lte=p2)
        )
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)



