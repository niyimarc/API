from django.contrib import admin
from apiapp.views import GenericTestApi, GenericTestApiUpdate
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', GenericTestApi.as_view()),
    # path('generic/<int:pk>', GenericTestApiUpdate.as_view()), 
    path('api/<int:id>', GenericTestApiUpdate.as_view()),
]
