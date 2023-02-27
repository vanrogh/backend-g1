from rest_framework import serializers
from blogs.models import Blog


class BlogSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField(min_length=1, max_length=100, allow_null=False)
    owner = serializers.CharField(allow_null=True)

    def create(self, validated_data):
        blogs = Blog(**validated_data)
        blogs.save()
        return blogs

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance