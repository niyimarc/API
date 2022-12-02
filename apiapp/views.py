from django.http import JsonResponse
from rest_framework import generics
from .models import BlogPost
from .serializers import TestApiSerializer
from rest_framework import viewsets

# Create your views here.

class ViewsetTestApi(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = TestApiSerializer
