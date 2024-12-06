from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializers import PostSerializers, UserSerializer


class PostList(generics.ListCreateAPIView):
    """
    List and create blog posts.

    This view handles the listing of all blog posts and creation of new posts.
    Users can retrieve a list of posts or create a new post via a POST request.

    Methods:
        GET: Retrieve a list of all blog posts.
        POST: Create a new blog post.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializers


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a single blog post.

    This view provides the functionality to retrieve, update, or delete a specific
    blog post identified by its ID.

    Methods:
        GET: Retrieve a specific post by ID.
        PUT: Update a specific post by ID.
        DELETE: Delete a specific post by ID.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializers


class ProtectedDataView(APIView):
    """
    View to return protected data.

    This view is designed to return a protected message (e.g., sensitive data)
    that can only be accessed by authorized users.

    Methods:
        GET: Return a secret message.
    """

    def get(self, _request):
        data = {"message": "Some secret message!"}
        return Response(data)


class UserList(generics.ListCreateAPIView):
    """
    List and create users.

    This view handles the listing of all users and the creation of new users.
    It allows for viewing and creating user accounts.

    Methods:
        GET: Retrieve a list of all users.
        POST: Create a new user.
    """

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a single user.

    This view provides functionality to retrieve, update, or delete a user
    based on their unique user ID.

    Methods:
        GET: Retrieve a specific user by ID.
        PUT: Update a specific user by ID.
        DELETE: Delete a specific user by ID.
    """

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
