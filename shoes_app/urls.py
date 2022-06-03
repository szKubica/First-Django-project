from django.urls import path, include
from shoes_app.views import all_shoes, about_us, shoes_home
#from shoes_app.views import roksana

urlpatterns = [
    path('all/', all_shoes),
    path('about us/', about_us),
    path('home/', shoes_home)
]