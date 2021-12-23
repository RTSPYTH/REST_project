from rest_framework.routers import SimpleRouter
from .views import FavoriteAPIView

router = SimpleRouter()
router.register("", FavoriteAPIView, basename='favorite')

urlpatterns = []
urlpatterns += router.urls