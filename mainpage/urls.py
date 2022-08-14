

from unicodedata import name
from django.urls import path,include
from requests import request
from .import views

app_name='mainpage'

urlpatterns = [
    path('',views.index,name='index'),
    path('products/',views.products,name='products'),
    path('products/detail/<int:pk>',views.productdetailview.as_view(),name="detail"),
    path('products/products/add',views.add_product,name="add_product"),
    path('products/update/<int:id>',views.update_product,name='update_product'),
    path('delete/<int:id>',views.delete_product,name='delete_product'),
    path('products/list',views.my_listings,name='list'),
    path('payment/<int:id>',views.payments,name='payments'),
    path('success/', views.PaymentSuccessView.as_view(), name='success'),
    path('failed/', views.PaymentFailedView.as_view(), name='failed'),
#     path('api/checkout-session/<id>',views.create_checkout_session,name='api_checkout_session'),
 ]
