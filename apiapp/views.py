from django.http import JsonResponse
from rest_framework.views import APIView
from .models import BlogPost
from django.forms.models import model_to_dict

# Create your views here.

class TestApi(APIView):
    def get(self, request):
        # get all the data from the BlogPost model 
        content = BlogPost.objects.all()
        # get the value of the objects 
        content = content.values()
        # convert the object into a list 
        content = list(content)
        return JsonResponse({'data': content})

    def post(self, request):
        new_blog_post = BlogPost.objects.create(
            post_title = request.data["post_title"],
            post_category_id = request.data["post_category_id"],
            post_contents = request.data["post_contents"],
        )
        # the model_to_dict() convert the model into a dictionary
        return JsonResponse({"data": model_to_dict(new_blog_post)})
