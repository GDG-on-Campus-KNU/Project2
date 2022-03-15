from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from comments import views

urlpatterns = [
    path('', views.CommentList.as_view()),
    path('<int:pk>/', views.CommentDetail.as_view()),
    path('all/', views.CommentAll.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)