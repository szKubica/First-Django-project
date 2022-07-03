from django.urls import path, include
from shoes_app.views import all_shoes, create_shoes, edit_shoes, delete_shoes, homepage
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', all_shoes, name='all_shoes'),
    path('add/', create_shoes, name='create_shoes'),
    path('edit/<int:id>/', edit_shoes, name='edit_shoes'),
    path('delete/<int:id>/', delete_shoes, name='delete_shoes')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)