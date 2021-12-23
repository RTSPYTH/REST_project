from rest_framework import serializers
from .models import Product


class ProductSerializers(serializers.ModelSerializer):
    # created_by = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)

    class Meta:
        model = Product
        fields = '__all__'