from .models import Board
from .serializers import BoardSerializer
from rest_framework import generics


class BoardList(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
