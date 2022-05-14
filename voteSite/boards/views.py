import ast
import datetime

from django.utils import timezone
from comments.models import Comment
from comments.serializers import CommentSerializer
from .models import Board, Vote
from .serializers import BoardSerializer
from rest_framework import generics, permissions, status
from .permission import IsOwnerOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Case, When
from django.conf import settings
from django.db import models
from django.db.models import FloatField
from django.db.models.functions import Cast


class BoardList(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        query=Board.objects.all()
        # 만약 모든 object 에 대해 votedIndex 를 -1로 바꾸느라 시간이 너무 오래 걸리면 여기서 밑에까지 지우면 된다.
        vote_models = Vote.objects.filter(voter=self.request.user)
        for q in query:
            q.votedIndex=-1
        Board.objects.bulk_update(query, ['votedIndex'])
        query=Board.objects.all()
        for vote_model in vote_models:
            tt=query.get(pk=int(str(vote_model.boardId)[14:-1]))
            tt.votedIndex=vote_model.indexInBoard
            tt.save()
        # 여기까지
        return query

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        vote_texts=ast.literal_eval(serializer.data['voteText'])
        print(vote_texts[0])
        for ind,text in enumerate(vote_texts):
            Vote.objects.create(content=text[0],boardId=Board.objects.latest('id'),indexInBoard=ind)

class BoardCategoryList(generics.ListAPIView):
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        query=Board.objects.filter(category=self.kwargs.get('word'))
        return query

class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_object(self):
        queryset=self.get_queryset()
        obj = queryset.get(pk=self.kwargs.get('pk'))
        vote_models = Vote.objects.filter(boardId=self.kwargs.get('pk'))
        obj.votedIndex=-1
        obj.currentUser=str(self.request.user)
        if self.request.user.is_authenticated:
            for ind, vote_model in enumerate(vote_models):
                if self.request.user in vote_model.voter.all():
                    obj.votedIndex=ind
                    break
            obj.save()
        return obj

    def destroy(self, request, *args, **kwargs):
        if self.request.user == self.get_object().owner:
            self.get_object().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)


class LikeBoard(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, pk):
        # print(request.get_full_path())
        current_board=Board.objects.get(id=pk)
        like_count_before=current_board.liker.all().count()
        current_board.liker.add(self.request.user)
        current_board.likeCount = current_board.liker.all().count()
        if current_board.likeCount!=like_count_before:
            current_board.save()
            return Response("successfully liked the board")
        else:
            return Response("already liked the board")


class VoteBoard(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, pk):
        user_voted_board_list= ast.literal_eval(request.user.profile.votedBoards)
        index=int(request.data['index'])
        vote_models=Vote.objects.filter(boardId=pk)
        board_model=Board.objects.get(id=pk)
        vote_texts = ast.literal_eval(board_model.voteText)
        if pk in user_voted_board_list:
            board_model.voteTotal-=1
            user_voted_board_list.remove(pk)
        for ind, vote_model in enumerate(vote_models):
            if self.request.user in vote_model.voter.all():
                vote_model.voter.remove(self.request.user)
                vote_texts[ind][1]-=1
            elif ind==index:
                vote_model.voter.add(self.request.user)
                vote_texts[ind][1]+=1
                user_voted_board_list.insert(0, pk)
                board_model.voteTotal+=1
            vote_model.save()
        request.user.profile.votedBoards = str(user_voted_board_list)
        request.user.profile.save()
        board_model.voteText=str(vote_texts)
        board_model.save()
        return Response(board_model.voteText)




class HotBoard(generics.ListAPIView):
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # timezone 이 조금 달라서, 15시간 전이 24시간 전까지 임. 3일 전까지로 하려면 days 를 2로 해야 함
        queryset = Board.objects.filter(createdAt__gte=(timezone.now() - datetime.timedelta(days=2,hours=15)))
        print(timezone.now() - datetime.timedelta(days=0,hours=15))
        queryset = queryset.order_by('-likeCount')[0:5]
        print(queryset)
        return queryset


class MyBoardList(generics.ListCreateAPIView):
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        queryset = Board.objects.filter(owner=user)
        return queryset


class CommentList(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Comment.objects.filter(boardId=self.kwargs['pk']).reverse()
        return queryset


class RecentlyVotedBoardList(generics.ListCreateAPIView):
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user_voted_board_list= ast.literal_eval(self.request.user.profile.votedBoards)
        boards = Board.objects.filter(id__in=user_voted_board_list)
        print(boards)
        # arr = []
        # for board in boards:
        #     if board.id not in arr:
        #         arr.append(board.id)
        # preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(arr)])
        return boards