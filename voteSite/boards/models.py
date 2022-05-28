from django.db import models


class Board(models.Model):
    categoryType = models.TextChoices('categoryType', "Love Travel Fashion Political Balance_Game Free")
    category = models.CharField(choices=categoryType.choices, max_length=30)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to="uploads")
    owner = models.ForeignKey('auth.user', related_name='owner_board', on_delete=models.CASCADE)
    liker = models.ManyToManyField('auth.user', related_name='liker_board')
    likeCount = models.IntegerField(default=0)
    votedIndex=models.IntegerField(default=-1)
    voteText = models.CharField(max_length=200)
    voteTotal=models.IntegerField(default=0)
    currentUser = models.TextField(default="None")

    class Meta:
        ordering = ['-createdAt']


class Vote(models.Model):
    content = models.TextField()
    voter = models.ManyToManyField('auth.user', related_name='voter_board')
    boardId = models.ForeignKey('boards.Board', related_name='vote_board_id', on_delete=models.CASCADE)
    indexInBoard=models.IntegerField(default=0)

    class Meta:
        ordering = ['boardId']
