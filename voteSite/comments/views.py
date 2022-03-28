from comments.models import Comment
from boards.models import Board
from comments.serializers import CommentSerializer
from boards.serializers import BoardSerializer
from rest_framework import generics
from rest_framework import permissions
from users.models import Profile
from comments.permissions import IsOwnerOrReadOnly
from django.db.models import Case, When


class CommentList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.request.method=="GET":
            return BoardSerializer
        else:
            return CommentSerializer

    def get_queryset(self):
        user = self.request.user
        comments=Comment.objects.filter(owner=user)
        arr=[]
        for comment in comments:
            if comment.boardId.id not in arr:
                arr.append(comment.boardId.id)
        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(arr)])
        return Board.objects.filter(pk__in=arr).order_by(preserved)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        profile = Profile.objects.get(user=self.request.user)
        profile.count+=1
        profile.save()


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_destroy(self, serializer):
        print("------------------------wow",self.request.user)
        profile = Profile.objects.get(user=self.request.user)
        profile.count-=1
        profile.save()
        serializer.delete()


class CommentAll(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]