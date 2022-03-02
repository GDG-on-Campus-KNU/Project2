from django.db import models


class Board(models.Model):
    category = models.CharField(max_length=50)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    recommend = models.IntegerField()

    class Meta:
        ordering = ['createdAt']
