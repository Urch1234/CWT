from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post


class PostSerializers(serializers.ModelSerializer):
    """
    Serializer for the Post model.

    This serializer is responsible for converting Post model instances into
    JSON format and validating data when creating or updating a Post.

    Attributes:
        Meta:
            - model: Specifies the model to serialize (Post).
            - fields: Defines the fields to include in the serialized output.
              These fields include 'id', 'author', 'title', 'content', and
              'created_at'.
    """

    class Meta:
        model = Post
        fields = ("id", "author", "title", "content", "created_at")


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.

    This serializer is responsible for converting User model instances into
    JSON format and validating data when creating or updating a User.

    Attributes:
        Meta:
            - model: Specifies the model to serialize (User).
            - fields: Defines the fields to include in the serialized output.
              These fields include 'id' and 'username'.
    """

    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "username",
        )
