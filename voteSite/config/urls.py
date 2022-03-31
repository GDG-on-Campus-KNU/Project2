from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('comments/', include('comments.urls')),
    path('boards/', include('boards.urls')),
    path('api/', include('auth_token.urls'))
]

urlpatterns += [
    path("docs/json/", SpectacularJSONAPIView.as_view(), name="schema-json"),
    # path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # path('schema/user', SpectacularAPIView.as_view(), name='user_schema'),
    path('schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema-json'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema-json'), name='redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
