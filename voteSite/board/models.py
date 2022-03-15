from django.db import models


class Board(models.Model):
    category = models.CharField(max_length=50)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    recommend = models.IntegerField()
    author = models.CharField(max_length=100)
    owner = models.ForeignKey('auth.user', related_name='boards', on_delete=models.CASCADE)

    choiceList = [] # get.object.all()

    class Meta:
        ordering = ['createdAt']

    def __str__(self):
        return self.content


class Choice(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.text


