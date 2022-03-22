from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('vote/', include('vote.urls')),
    path('', include('users.urls')),
    path('comments/', include('comments.urls')),
    path('boards/', include('board.urls')),
    path('api/', include('auth_token.urls'))
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
