# DjangoProject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 'accounts/' 주소를 django가 미리 만들어둔 인증 앱에 연결합니다.
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('courses.urls')),
]