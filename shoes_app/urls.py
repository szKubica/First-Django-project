from django.urls import path, include
from shoes_app.views import all_shoes, about_us, shoes_home, create_shoes, edit_shoes
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('all/', all_shoes),
    path('about us/', about_us),
    path('home/', shoes_home),
    path('add/', create_shoes),
    path('edit/<int:id>/', edit_shoes)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)