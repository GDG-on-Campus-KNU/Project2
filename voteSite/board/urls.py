from django.urls import path
from .views import BoardList, BoardDetail

urlpatterns = [
    path('', BoardList.as_view()),
    path('<int:pk>/', BoardDetail.as_view()),
]
