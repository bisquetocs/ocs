from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.forms import UserCreationForm

#app_name = 'accounts'
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('register/check', views.registerUser, name='registerUser'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', views.profile, name='profile'),
    path('empleados/', views.EmpleadosView.as_view(), name='empleados'),
    path('empleados/registro/', views.RegisterView.as_view(), name='registro'),
    path('vote/', views.vote, name='vote'),

]
