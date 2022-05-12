from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('users/current/', views.UserCurrent.as_view()),
    # path('users/reg/', views.CreateUserView.as_view()),
    path('register/', views.UserCreate.as_view()),
    path('delete/', views.UserDelete.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)