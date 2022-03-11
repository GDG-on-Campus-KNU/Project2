from django.conf import settings
from django.db import models


class Profile(models.Model):
    count = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']