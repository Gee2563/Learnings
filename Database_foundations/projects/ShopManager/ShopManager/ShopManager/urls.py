from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("shop/", include("stockIorders.urls")),
    path("admin/", admin.site.urls),
]