from rest_framework import serializers

class TestApiSerializer(serializers.Serializer):
    post_title = serializers.CharField()
    post_category_id = serializers.IntegerField()
    created_date = serializers.DateTimeField(read_only=True)
    updated_on = serializers.DateTimeField(read_only=True)
    post_contents = serializers.CharField()



