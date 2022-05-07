from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer
from .models import Comment


class CommentSerializer(ModelSerializer):
    comment_author = StringRelatedField()

    class Meta:
        model = Comment
        # fields = ['comment_post', 'comment_text']
        fields = '__all__'
