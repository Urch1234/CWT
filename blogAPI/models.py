from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    A model representing a blog post.

    This model stores the information about a blog post, including its title,
    content, author (linked to the User model), and timestamps for creation
    and last update.

    Attributes:
        title (str): The title of the blog post (max 100 characters).
        content (str): The content of the blog post (unlimited text).
        author (ForeignKey): A reference to the user who created the post.
        created_at (datetime): The timestamp when the post was created.
        updated_at (datetime): The timestamp when the post was last updated.

    Methods:
        __str__(): Returns the title of the post when it is displayed.
    """

    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Return a string representation of the Post object.

        This method returns the title of the blog post as a string,
        which is used when displaying the object in the Django admin or other views.

        Returns:
            str: The title of the blog post.
        """
        return self.title
