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

        new_blog_post = BlogPost.objects.create(
            post_title = request.data["post_title"],
            post_category_id = request.data["post_category_id"],
            post_contents = request.data["post_contents"],
        )
        # the model_to_dict() convert the model into a dictionary
        return JsonResponse({"data": TestApiSerializer(new_blog_post).data})
