from django.urls import path
from . import views

urlpatterns = [
#Main 
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('user/', views.userPage, name='userPage'),

#------------------------------------------------------------------------------
#Order Info
    path('create_order/<str:pk>/', views.createOrder, name='create_order'),
    path('update_order/<str:pk>/', views.updateOrder, name='update_order'),
    path('create_customer/', views.createCustomer, name='create_customer'),
    path('delete_order/<str:pk>', views.deleteOrder, name='delete_order' ),

#------------------------------------------------------------------------------
#Login and Logout
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout')
]
