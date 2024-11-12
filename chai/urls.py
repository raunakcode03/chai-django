from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_chai, name='all_chai'),  
    path('orders/', views.order_summary, name='order_summary'),
    path('order-chai/', views.order_chai, name='order_chai'),  # Order placement page
    path('chai/<int:chai_id>/', views.chai_detail, name='chai_detail'),  # Chai detail view
    path('sync-orders/', views.sync_orders, name='sync_orders'),  # Sync orders with session
]
