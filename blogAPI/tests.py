from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post


class BlogTest(TestCase):
    """
    Test case for the Blog application.

    This class contains tests for the blog's functionality, specifically the
    creation of blog posts and their associated content. The tests ensure that
    the blog post is created with the correct author, title, and content.

    Methods:
        setUpTestData: Creates a test user and a test post for use in the tests.
        test_blog_content: Validates that the created blog post has the correct
                           author, title, and content.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up test data for the blog.

        This method creates a test user (`testuser1`) and a blog post associated
        with this user. The user and post are stored in the database and used
        for subsequent test methods.
        """
        # Create a user
        testuser1 = User.objects.create_user(
            username="testuser1", password="password123"
        )
        testuser1.save()

        # Create a blog post
        test_post = Post.objects.create(
            author=testuser1, title="Blog title", content="Nice content ..."
        )
        test_post.save()

    def test_blog_content(self):
        """
        Test the content of the blog post.

        This method checks if the blog post created in `setUpTestData` has the
        expected author, title, and content. It ensures that the blog post is
        properly created and the data is accurate.

        Assertions:
            - The post author should be 'testuser1'.
            - The post title should be 'Blog title'.
            - The post content should be 'Nice content ...'.
        """
        post = Post.objects.get(id=1)
        author = f"{post.author}"
        title = f"{post.title}"
        content = f"{post.content}"
        self.assertEqual(author, "testuser1")
        self.assertEqual(title, "Blog title")
        self.assertEqual(content, "Nice content ...")
