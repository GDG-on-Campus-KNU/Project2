from django.http import JsonResponse
from snippets.models import Snippet, Profile
from snippets.serializers import SnippetSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer
from rest_framework import permissions

from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.generics import CreateAPIView

from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        profile = Profile.objects.get(user=self.request.user)
        profile.count+=1
        profile.save()
        print("----------", profile, profile.user,profile.count)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def perform_destroy(self, serializer):
        print("------------------------wow",self.request.user)
        profile = Profile.objects.get(user=self.request.user)
        profile.count-=1
        profile.save()


class UserDelete(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user=self.request.user
        user.delete()

        return JsonResponse({"result":"user delete"})
