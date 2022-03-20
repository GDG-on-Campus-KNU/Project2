from .models import Board
from .serializers import BoardSerializer
from rest_framework import generics, permissions
from .permission import IsOwnerOrReadOnly


class BoardList(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # def perform_update(self, serializer):
    #     board_id = self.kwargs['pk']
    #     current_board=Board.objects.get(id=board_id)
    #     current_board.likeCount= current_board.liker.all().count()
    #     current_board.save()


class LikeBoard(generics.RetrieveAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        board_id = self.kwargs['pk']
        current_board=Board.objects.get(id=board_id)
        current_board.liker.add(self.request.user)
        current_board.likeCount = current_board.liker.all().count()
        current_board.save()
