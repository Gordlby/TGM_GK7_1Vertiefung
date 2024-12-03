from django.urls import path
from . import views

urlpatterns = [
    path('fach', views.mainfach, name='mainFach'),
    path('fach/<int:fachid>', views.specfach, name='specFach'),
    path('antwort', views.choicemain, name='antwort'),
    path('antwort/<int:antwortid>', views.specchoice, name='choicemain')
]