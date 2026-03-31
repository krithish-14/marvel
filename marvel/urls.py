from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('characters/', views.characters, name='characters'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('password/', views.password, name='password'),
    path('cm/', views.cm, name='cm'),
]
