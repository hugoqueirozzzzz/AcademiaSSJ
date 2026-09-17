from django.urls import path
from .views import home

app_name = "academia_modulo"

urlpatterns = [
    path('', home, name='home'),
]