from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('home/', views.home, name='home'),
    path('registrar/', views.registrar, name='registrar'),
    path('visualizar/', views.visualizar, name='visualizar'),
]