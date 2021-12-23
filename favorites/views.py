from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Favorite

from .serializers import FavoriteSerializers
from .permissions import IsOwnerOnly


class FavoritePagination(PageNumberPagination):
    page_size = 10


class FavoriteAPIView(viewsets.ModelViewSet):
    serializer_class = FavoriteSerializers
    permission_classes = [IsOwnerOnly]
    queryset = Favorite.objects.all()

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)
