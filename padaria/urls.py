from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("paes/", include("paes.urls")),
    path('admin/', admin.site.urls),
]
