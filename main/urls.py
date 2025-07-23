from django.urls import path
from .views import home, search, cart

urlpatterns = [
    path('', home, name='home'),
    path('search/', search, name='search'),
    path('cart/', cart, name='cart'),
]
