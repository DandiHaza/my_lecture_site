# DjangoProject/urls.py

from django.contrib import admin
from django.urls import path, include

# settings.py에서 MEDIA_URL, MEDIA_ROOT를 가져오기 위해 import 합니다.
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('courses.urls')),
]

# 개발 모드에서만 미디어 파일을 서빙하도록 추가합니다. (배포 시에는 웹 서버가 처리)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)