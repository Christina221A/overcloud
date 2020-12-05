from django.urls import path

from . import views

app_name = 'webapp'
urlpatterns = [
    # ex: /webapp/
    path('', views.index, name='index'),
    # ex: /webapp/5/
    path('<int:product_id>/', views.detail, name='detail'),
    # ex:/webapp/signIn
    path('signIn/', views.signIn, name='signIn'),
]