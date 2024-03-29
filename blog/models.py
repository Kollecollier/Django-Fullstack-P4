"""
Database models for the blog app
& comments section.
"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


# Model provided from "I think therefore I blog" walkthrough, with custom changes.
class Post(models.Model):
    blog_title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    blog_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    blog_content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.blog_title

    def number_of_likes(self):
        return self.likes.count()


# Model provided from "I think therefore I blog" walkthrough, made custom changes.
class Comment(models.Model):
    blog_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"comment {self.message} by {self.user.username}"
