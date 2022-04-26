from rest_framework import serializers


class DataSerializer(serializers.Serializer):
    id = serializers.CharField()
    code = serializers.CharField()
    username = serializers.CharField(max_length=100)
    comment_count = serializers.IntegerField()
    like_count = serializers.IntegerField()
    caption_text = serializers.CharField(max_length=40000)
    thumbnail_url = serializers.JSONField()
    view_count = serializers.IntegerField()
    media_type = serializers.IntegerField()
    resources = serializers.JSONField(required=False)