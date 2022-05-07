from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Like


class LikeSerializer(ModelSerializer):
    # user = StringRelatedField()

    class Meta:
        model = Like
        fields = ['id', 'content_id']
        # fields = '__all__'
