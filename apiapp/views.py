from django.http import JsonResponse
from rest_framework.views import APIView
from .models import BlogPost
from .serializers import TestApiSerializer

# Create your views here.

class TestApi(APIView):
    def get(self, request):
        # get all the data from the BlogPost model 
        content = BlogPost.objects.all()
        # many=True will tell the serializer that the data is an object 
        return JsonResponse({'data': TestApiSerializer(content, many=True).data})

    def post(self, request):
        # request.data is the data we want to validate before posting 
        serializer = TestApiSerializer(data=request.data)
        # is_valid will check based on what will define in our TestApiSerializer 
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({"data": serializer.data})

    def put(self, request, *args, **kwargs):
        # incase id doesnt exist use None as the default value 
        model_id = kwargs.get("id", None)
        if not model_id:
            return JsonResponse({"error": "method /PUT/ is not allowed."})
        try:
            instance = BlogPost.objects.get(id=model_id)
        except:
            return JsonResponse({"error": "object does not exist."})
        serializer = TestApiSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({"data": serializer.data})
