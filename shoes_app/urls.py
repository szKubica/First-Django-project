from django.urls import path, include
from shoes_app.views import all_shoes, about_us, shoes_home
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('all/', all_shoes),
    path('about us/', about_us),
    path('home/', shoes_home)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)