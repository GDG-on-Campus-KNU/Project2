from django.db import models


class Comment(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='owner_comment', on_delete=models.CASCADE)
    boardId = models.ForeignKey('boards.Board', related_name='comment_board_id', on_delete=models.CASCADE)

    class Meta:
        ordering = ['createdAt']
