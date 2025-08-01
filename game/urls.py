from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),  # <- this is required
]
