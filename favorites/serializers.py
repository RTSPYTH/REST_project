from rest_framework import serializers
from .models import Favorite


class FavoriteSerializers(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = '__all__'

