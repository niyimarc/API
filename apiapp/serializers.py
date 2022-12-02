from rest_framework import serializers
from .models import BlogPost


# use ModelSerializer to make use of the fields in the model directly 
class TestApiSerializer(serializers.ModelSerializer):
    class Meta:
        # the model you want to work on 
        model = BlogPost
        # the specific fields you want to output 
        # fields = ("post_title", "post_category", "post_contents",) 
        # if you want all the fields in the model to be output
        fields = "__all__"






