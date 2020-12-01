from django.urls import path

from . import views

app_name = 'webapp'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /webapp/5/
    path('<int:product_id>/', views.detail, name='detail'),
]