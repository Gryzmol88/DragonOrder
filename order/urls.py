from django.urls import path
from . import views

app_name = 'order'
urlpatterns = [
    path('', views.index, name='index'),
    path('order_list/', views.order_list, name='order_list'),
    path('order_list/<int:order_id>/', views.order_products, name='order_products'),
]
