from django.urls import path
from .views import *

urlpatterns = [
    path('', BoardList.as_view()),

    path('love', LoveBoardList.as_view()),
    path('travel', TravelBoardList.as_view()),
    path('fashion', FashionBoardList.as_view()),

    path('<int:pk>/', BoardDetail.as_view()),
    path('<int:pk>/like/', LikeBoard.as_view()),
    path('<int:pk>/vote/', VoteBoard.as_view()),
]

