from django.conf import settings
from django.db import models


class Profile(models.Model):
    count = models.IntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    votedBoards = models.CharField(max_length=500, null=True, default="[]")
    image = models.ImageField(upload_to='users/image', default='users/image/default_image.png')

    class Meta:
        ordering = ['createdAt']