from rest_framework import serializers
from .models import BlogPost

class TestApiSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    post_title = serializers.CharField()
    post_category_id = serializers.IntegerField()
    created_date = serializers.DateTimeField(read_only=True)
    updated_on = serializers.DateTimeField(read_only=True)
    post_contents = serializers.CharField()

    # create a new post with the serializer 
    def create(self, validated_data):
        # validated_data is the data validated by the serializer 
        return BlogPost.objects.create(**validated_data)

    # update a post with the serializer 
    def update(self, instance, validated_data):
        BlogPost.objects.filter(id = instance.id).update(**validated_data)
        return BlogPost.objects.get(id = instance.id)






