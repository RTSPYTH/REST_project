from django.shortcuts import render

# Create your views here.
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Order
from .permissions import IsOwnerOnly
from .serializers import OrderSerializers
from products.models import Product


class OrderAPIView(viewsets.ModelViewSet):
    serializer_class = OrderSerializers
    permission_classes = [IsOwnerOnly]
    queryset = Order.objects.all()

    def list(self, request, *args, **kwargs):
        owner = request.user
        query = Order.objects.filter(ordered_by=owner)
        serializer = OrderSerializers(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save(ordered_by=self.request.user)
        count = self.request.data.get('count')
        product_id = self.request.data.get('product_id')
        product = Product.objects.filter(id=product_id).first()
        total_price = product.price * count
        product.quantity = product.quantity - count
        product.save()
        order = Order.objects.create(total_price=total_price, product_id=product, count=count)
        serializer = OrderSerializers(order)

        return Response(serializer.data)