from django.contrib import admin
from django.urls import path, include
from vote import views
from board import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('vote/', include('vote.urls')),
    path('board/', include('board.urls'))
]
