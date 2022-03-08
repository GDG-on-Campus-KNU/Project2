from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    # path('users/reg/', views.CreateUserView.as_view()),
    path('account/register/', views.UserCreate.as_view()),
    path('account/delete/', views.UserDelete.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)