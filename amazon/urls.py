from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('add/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('increase/<int:id>/', views.increase, name='increase'),
    path('decrease/<int:id>/', views.decrease, name='decrease'),
    path('remove/<int:id>/', views.remove, name='remove'),
    path('register/<int:id>/', views.remove, name='register'),
    path('login/<int:id>/', views.remove, name='login'),
    path('logout/<int:id>/', views.remove, name='logout'),
    path('checkout/<int:id>/', views.remove, name='checkout'),
]
