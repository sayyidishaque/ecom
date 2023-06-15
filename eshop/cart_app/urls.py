from django.urls import path
from . import views

app_name = 'cart_app'
urlpatterns = [
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('', views.cart_details, name='cart_details'),
    path('cart_remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('remove_all/<int:product_id>/', views.remove_all, name='remove_all'),
]
