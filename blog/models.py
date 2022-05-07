from django.contrib.auth.models import User
from django.db import models
from profiles.models import Profile


class Post(models.Model):
    label = models.CharField(max_length=100, db_index=True)
    text = models.CharField(max_length=10000, db_index=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='post_for_user')
    date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.label
