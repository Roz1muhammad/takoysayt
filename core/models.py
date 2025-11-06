from django.db import models

from .auth_models import User



class Post(models.Model):
    title = models.CharField(max_length=256)
    decs = models.TextField()
    image = models.ImageField(upload_to="posts/", null=True, blank=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey("core.User", on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)







