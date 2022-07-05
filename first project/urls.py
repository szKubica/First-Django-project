from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from shoes_app.views import all_shoes




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('shoes_app.urls')),
    path('user/', include('user_login.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
