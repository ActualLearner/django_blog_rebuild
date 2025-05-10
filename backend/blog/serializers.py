from rest_framework import serializers
from .models import *

class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    comments = serializers.HyperlinkedRelatedField(many=True, view_name='comment-detail', read_only=True)
    
    class Meta:
        model = Post
        fields = ['url', 'id', 'author', 'title', 'content', 'comments', 'created_at']
        
class CommentSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    post = serializers.HyperlinkedRelatedField(view_name='post-detail', queryset=Post.objects.all())
    
    class Meta:
        model = Comment
        fields = ['url', 'content', 'created_at', 'author', 'post']
        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)
    comments = serializers.HyperlinkedRelatedField(many=True, view_name='comment-detail', read_only=True)
    
    class Meta:
        model = User
        fields = ['url', 'username', 'posts', 'comments']