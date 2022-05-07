from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from rest_framework import generics
from post_comments.serializers import CommentSerializer
from post_likes.serializers import LikeSerializer
from .models import Post


class BlogSerializer(ModelSerializer):
    liked = SerializerMethodField()

    def get_liked(self, obj):
        return obj.likes_for_post.count()

    class Meta:
        model = Post
        fields = ['id', 'label', 'text', 'liked']


class PostSerializer(ModelSerializer):
    comment = CommentSerializer(many=True, required=False)
    liked = SerializerMethodField()

    def get_liked(self, obj):
        return obj.likes_for_post.count()

    class Meta:
        model = Post
        fields = '__all__'
