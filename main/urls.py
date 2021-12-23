from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('authentications.urls')),
    path('api/v1/category/', include('categories.urls')),
    path('api/v1/product/', include('products.urls')),
    path('api/v1/favorite/', include('favorites.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)