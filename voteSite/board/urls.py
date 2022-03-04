from django.urls import path
from .views import BoardList, BoardDetail, UserList, UserDetail

urlpatterns = [
    path('boards/', BoardList.as_view()),
    path('boards/<int:pk>/', BoardDetail.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>', UserDetail.as_view()),
]
