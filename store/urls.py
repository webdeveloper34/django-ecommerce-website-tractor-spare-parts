from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('product/<int:id>/', views.product_detail, name='product_detail'),  # Product detail
    path('cart/', views.cart, name='cart'),  # Cart page
    path('checkout/', views.checkout, name='checkout'),  # Checkout page
    path('search/', views.search, name='search'),  # Search page
]
