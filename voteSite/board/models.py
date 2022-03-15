from django.db import models


class Board(models.Model):
    category = models.CharField(max_length=50)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    recommend = models.IntegerField()
    author = models.CharField(max_length=100)
    owner = models.ForeignKey('auth.user', related_name='boards', on_delete=models.CASCADE)

    class Meta:
        ordering = ['createdAt']

class Vote(models.Model):
    board = models.OneToOneField(Board,on_delete=models.CASCADE)

class Choice(models.Model):
    vote = models.ForeignKey(Vote,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name




