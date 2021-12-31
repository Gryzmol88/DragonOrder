from django.urls import path
from . import views

app_name = 'order'
urlpatterns = [
    path('', views.index, name='index'),
    path('order_list/', views.order_list, name='order_list'),
    path('order/<int:order_id>/', views.order_products, name='order_products'),
    path('new_order/', views.new_order, name='new_order'),
    path('new_product/<int:order_id>/', views.new_product, name='new_product'),
    path('edit_order/<int:order_id>/', views.edit_order, name='edit_order'),
    path('delete_order/<int:order_id>/', views.delete_order, name='delete_order'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),

]
