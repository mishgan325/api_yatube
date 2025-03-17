from rest_framework import serializers
from posts.models import Group, Post, Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "title", "slug", "description")
        model = Group


class PostSerializer(serializers.ModelSerializer):
    author = (
        serializers.SlugRelatedField(
            slug_field="username", read_only=True))

    class Meta:
        model = Post
        fields = ("id", "text", "author", "image", "group", "pub_date")


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ["id", "author", "post", "text", "created"]
        read_only_fields = ["author", "post"]

    def get_author(self, obj):
        return obj.author.username if obj.author else None
