from django.db import models


class Board(models.Model):
    category = models.CharField(max_length=50)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to="uploads")
    owner = models.ForeignKey('auth.user', related_name='boards', on_delete=models.CASCADE)
    liker = models.ManyToManyField('auth.user', related_name='liker_board')
    likeCount = models.IntegerField(default=0)

    class Meta:
        ordering = ['createdAt']


# class Vote(models.Model):
#     createdAt = models.DateTimeField(auto_now_add=True)
#     count=models.IntegerField()
#     content = models.TextField()
#     voter = models.ManyToManyField('auth.user', related_name='boards')
#     board_id = models.ForeignKey('boards.Board', related_name='doard_id', on_delete=models.CASCADE)
#
#     class Meta:
#         ordering = ['createdAt']
