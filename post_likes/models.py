from django.contrib.auth.models import User
from django.db import models
from blog.models import Post


class Like(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='likes')
    content_id = models.ForeignKey(Post,
                                   on_delete=models.CASCADE,
                                   related_name='likes_for_post')

    def __str__(self):
        return str(self.content_id) + " (" + str(self.user) + ")"
