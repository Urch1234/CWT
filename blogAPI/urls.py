from django.urls import path
from .views import PostList, PostDetail, ProtectedDataView, UserList, UserDetail

urlpatterns = [
    # Blog post endpoints
    path("posts/", PostList.as_view(), name="post-list"),  # List and create posts
    path(
        "posts/<int:pk>/", PostDetail.as_view(), name="post-detail"
    ),  # Get, update, and delete post by ID
    # User endpoints
    path("users/", UserList.as_view(), name="user-list"),  # List and create users
    path(
        "users/<int:pk>/", UserDetail.as_view(), name="user-detail"
    ),  # Get, update, and delete user by ID
    # Protected data endpoint
    path(
        "protected/", ProtectedDataView.as_view(), name="protected-data"
    ),  # Example protected endpoint
]
