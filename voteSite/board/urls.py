from django.urls import path
from .views import BoardList, BoardDetail

urlpatterns = [
    path('boards/', BoardList.as_view()),
    path('boards/<int:pk>/', BoardDetail.as_view()),
]
