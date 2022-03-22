import ast
from .models import Board, Vote
from .serializers import BoardSerializer
from rest_framework import generics, permissions
from .permission import IsOwnerOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response


class BoardList(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        vote_texts=ast.literal_eval(serializer.data['voteText'])
        print(vote_texts[0])
        for ind,text in enumerate(vote_texts):
            Vote.objects.create(content=text[0],boardId=Board.objects.latest('id'),indexInBoard=ind)


class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_object(self):
        queryset=self.get_queryset()
        obj = queryset.get(pk=self.kwargs.get('pk'))
        vote_models = Vote.objects.filter(boardId=self.kwargs.get('pk'))
        obj.votedIndex=-1
        print(self.request.user.is_authenticated)
        if self.request.user.is_authenticated:
            for ind, vote_model in enumerate(vote_models):
                if self.request.user in vote_model.voter.all():
                    obj.votedIndex=ind
                    break
            obj.save()
        return obj


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
        # print(request.get_full_path())
        index=request.data['index']
        print(request.data['index'])
        vote_models=Vote.objects.filter(boardId=pk)
        board_model=Board.objects.get(id=pk)
        vote_texts = ast.literal_eval(board_model.voteText)
        for ind, vote_model in enumerate(vote_models):
            if self.request.user in vote_model.voter.all():
                vote_model.voter.remove(self.request.user)
                vote_texts[ind][1]-=1
            elif ind==index:
                vote_model.voter.add(self.request.user)
                vote_texts[ind][1]+=1
            vote_model.save()
        board_model.voteText=str(vote_texts)
        board_model.save()
        return Response(board_model.voteText)
