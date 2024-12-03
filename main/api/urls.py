from django.urls import path
from . import views

urlpatterns = [
    path('fach', views.mainfach, name='mainFach'),
    path('fach/<int:fachid>', views.specfach, name='specFach')
]