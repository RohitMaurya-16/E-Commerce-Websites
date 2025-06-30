from django.urls import path
from . import views

# This makes it easier to reference the app's urls
app_name = 'shop'

urlpatterns = [
    path('info/', views.profile_info, name='profile_info'),
    path('orders/', views.profile_orders, name='profile_orders'),
    path('payments/', views.profile_payments, name='profile_payments'),
    path('addresses/', views.profile_addresses, name='profile_addresses'),
    path('wishlist/', views.profile_wishlist, name='profile_wishlist'),
    path('security/', views.profile_security, name='profile_security'),
    path('preferences/', views.profile_preferences, name='profile_preferences'),
    # Redirect base /profile/ to the info page
    path('', views.profile_info, name='profile_redirect'),
] 