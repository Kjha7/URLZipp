from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.encodeUrl, name='home'),
    path('<int:id_>', views.get_original_url, name='original_url')
]