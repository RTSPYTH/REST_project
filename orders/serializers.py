from rest_framework import serializers
from .models import Order


class OrderSerializers(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = [
                    'product_id', 'count'
                    ]