from django.db import models


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    board_id = models.ForeignKey('boards.Board', related_name='board_id', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
