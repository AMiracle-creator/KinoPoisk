from rest_framework import serializers

from main.models import Comment, KinopoiskUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = KinopoiskUser
        fields = ('id', 'name', 'email')


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Comment
        fields = ('author', 'text', 'movie')


class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('movie', 'author', 'text')
