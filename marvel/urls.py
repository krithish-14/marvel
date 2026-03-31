from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('characters/', views.characters, name='characters'),
    path('login/', views.login, name='login'),
    path('password/', views.password, name='password'),
    path('cm/', views.cm, name='cm'),
]
