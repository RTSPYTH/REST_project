from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Favorite

from .serializers import FavoriteSerializers
from .permissions import IsOwnerOnly


class FavoritePagination(PageNumberPagination):
    page_size = 10


class FavoriteAPIView(viewsets.ModelViewSet):
    serializer_class = FavoriteSerializers
    permission_classes = [IsOwnerOnly]
    queryset = Favorite.objects.all()

    def list(self, request, *args, **kwargs):
        owner = request.user
        query = Favorite.objects.filter(added_by=owner)
        serializer = FavoriteSerializers(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)
