from django.db import models


class Board(models.Model):
    category = models.CharField(max_length=50)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    content = models.TextField()
    recommend = models.IntegerField()
