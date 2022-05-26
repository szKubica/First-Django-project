from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls)
    path('shoes/', include('shoes_app.url'))
]
