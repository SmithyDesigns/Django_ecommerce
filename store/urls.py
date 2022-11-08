from django.urls import path
from . import views


urlpatterns = [
    #     base url to be included
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('login/', views.user_login, name='login_page'),
    path('authenticating/', views.authenticate_user, name='authenticate_login'),
    path('logout/', views.log_out_view, name='logout_page'),

]
