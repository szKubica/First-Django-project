from django.urls import path, include
from shoes_app.views import test
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test),
]