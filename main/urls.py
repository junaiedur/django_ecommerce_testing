from django.urls import path
from .views import home, search, cart, login_view, signup_view

urlpatterns = [
    path('', home, name='home'),
    path('search/', search, name='search'),
    path('cart/', cart, name='cart'),

    # 🔐 Login Page
    path('login/', login_view, name='login'),

    # Signup Page
    path('signup/', signup_view, name='signup'),
]
