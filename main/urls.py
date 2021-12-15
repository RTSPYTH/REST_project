from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('authentications.urls')),
    path('api/v1/category/', include('categories.urls')),
    # path('api/v1/store_app/', include('store_app.urls')),
]