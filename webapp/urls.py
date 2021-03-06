from django.urls import path

from . import views

app_name = 'webapp'
urlpatterns = [
    # ex: /webapp/
    path('', views.index, name='index'),
    # ex: /webapp/5/
    path('<int:product_id>/', views.detail, name='detail'),
    # ex: /webapp/signIn
    path('sign_in/', views.sign_in, name='sign_in'),
    # ex: /webapp/cart
    path('cart/', views.cart, name='cart'),
    # ex: /webapp/menu
    path('menu/', views.menu, name='menu'),
    # ex: /webapp/add_count
    path('add_count/', views.add_count, name='add_count'),
    # ex: /webapp/min_count
    path('min_count/', views.min_count, name='min_count'),
]
