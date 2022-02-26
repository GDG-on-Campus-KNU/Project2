from django.contrib import admin
from django.urls import path, include
from vote import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('vote/', include('vote.urls')),
]
