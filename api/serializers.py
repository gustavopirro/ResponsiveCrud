from rest_framework import serializers
from api.models import Post
from django.contrib.auth.models import User

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    updated = serializers.BooleanField(default=False, read_only=True)

    class Meta:
        model = Post
        fields = ['title', 'content', 'creation_date', 'updated', 'updated_at', 'author']
    
    
    def create(self, validated_data):
        author = self.context['request'].user
        new_post = Post.objects.create(**validated_data, author=author)
        return new_post