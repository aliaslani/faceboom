from django.db import models

class Post(models.Model):
    author = models.ForeignKey('usermanagement.CustomUser', on_delete=models.CASCADE, related_name='user_posts')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
