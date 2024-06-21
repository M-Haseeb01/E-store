from django.urls import path
from .views import registerpage, login_view, home,product_list,add_to_cart, cart_view

urlpatterns = [
    path('register/', registerpage, name='register'),
    path('', login_view, name='login'),
    path('home/', home, name='home'),
    path('/shop',product_list,name='shop'),
     path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_view, name='cart'),
]
