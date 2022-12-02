from django.http import JsonResponse
from rest_framework import generics
from .models import BlogPost
from .serializers import TestApiSerializer

# Create your views here.

class GenericTestApi(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = TestApiSerializer

class GenericTestApiUpdate(generics.UpdateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = TestApiSerializer
    # we can specify our own lookup_field 
    # if we dont want to use the pk in the url 
    lookup_field = "id"