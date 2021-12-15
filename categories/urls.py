from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import CategoryAPIView

router = SimpleRouter()
router.register("", CategoryAPIView, basename='category' )

urlpatterns = []
urlpatterns += router.urls