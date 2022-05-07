from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer, StringRelatedField

from blog.models import Post
from post_likes.serializers import LikeSerializer
from .models import Profile
from django.contrib.auth.models import User


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(ModelSerializer):
    post_for_user = PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    public_user_info = ProfileSerializer()
    likes = LikeSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'
