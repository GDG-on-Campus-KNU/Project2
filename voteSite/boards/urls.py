from django.urls import path
from .views import BoardList, BoardDetail, LikeBoard

urlpatterns = [
    path('', BoardList.as_view()),
    path('<int:pk>/', BoardDetail.as_view()),
    path('<int:pk>/like/', LikeBoard.as_view()),
]
