from comments.models import Comment
from comments.serializers import CommentSerializer
from rest_framework import generics
from rest_framework import permissions
from users.models import Profile
from comments.permissions import IsOwnerOrReadOnly


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Comment.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        profile = Profile.objects.get(user=self.request.user)
        profile.count+=1
        profile.save()
        print("----------&&&&&&&&&________________")


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