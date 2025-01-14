from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='Fächer'),
    path('index/', views.index, name='Fächer'),
    path('detail/<int:fach_id>/', views.detail, name='Detail'),
    path('results/<int:fach_id>/', views.results, name='Ergebinsse'),
    path('fachadd/', views.fachadd, name='Fach hinzufügen'),
    path('api/', include('main.api.urls')),
    path('login/', views.vlogin, name='login'),
    path('logout/', views.vlogout, name='logout'),
]