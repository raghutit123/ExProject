from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.title


class Comments(models.Model):
    body = models.TextField(max_length=200, null=False, blank=False)
    postId = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')


    def __str__(self):
        return self.body