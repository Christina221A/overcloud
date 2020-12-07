from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    # ex: /login/
    path('', views.index, name='index'),
    # ex:/login/signIn
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    
]