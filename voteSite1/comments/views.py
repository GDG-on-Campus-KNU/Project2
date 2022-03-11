from django.http import JsonResponse
from comments.models import Comment
from comments.serializers import CommentSerializer
from rest_framework import generics
from rest_framework import permissions
from users.models import Profile
from comments.permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        profile = Profile.objects.get(user=self.request.user)
        profile.count+=1
        profile.save()
        print("----------", profile, profile.user,profile.count)


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
