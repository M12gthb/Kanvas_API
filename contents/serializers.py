from rest_framework import serializers
from .models import Content


class Contentserializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ["id", "name", "video_url", "content"]
        read_only_fields = ["course", "video_url"]
