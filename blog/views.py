from .models import Post
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer, BlogSerializer
from rest_framework import generics
import datetime
from rest_framework import permissions


class BlogViewList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            date=datetime.datetime.now(),
            liked=0)


class BlogViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

