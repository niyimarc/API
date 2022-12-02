from django.contrib import admin
from apiapp.views import TestApi
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', TestApi.as_view()),
    path('api/<int:id>', TestApi.as_view())
]
