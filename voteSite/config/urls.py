from django.contrib import admin
from django.urls import path, include
# from ..vote import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('vote/', include('vote.urls')),
    path('', include('users.urls')),
    path('comments/', include('comments.urls')),
    path('boards/', include('board.urls'))
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
