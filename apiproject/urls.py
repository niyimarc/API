from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apiapp.views import ViewsetTestApi

router = DefaultRouter()
router.register("api", ViewsetTestApi)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
]
