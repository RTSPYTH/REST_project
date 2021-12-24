from rest_framework.routers import SimpleRouter
from .views import OrderAPIView

router = SimpleRouter()
router.register("", OrderAPIView, basename='favorite')

urlpatterns = []
urlpatterns += router.urls