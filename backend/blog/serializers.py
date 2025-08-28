from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
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
        
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user