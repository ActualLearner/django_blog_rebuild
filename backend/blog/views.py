from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        post = Post.objects.filter(pk=self.pk)
        serializer.save(author=self.request.user, post=post)
        
    def get_queryset(self):
        queryset = Comment.objects.all()
        post_id = self.request.query_params.get('post_id')
        if post_id is not None:
            queryset = queryset.filter(post_id=post_id)
        return queryset

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer