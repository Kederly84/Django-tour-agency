from django.urls import path

from ordersapp.apps import OrdersappConfig
from ordersapp.views import OrderList, OrderItemsCreate, OrderItemsUpdate, OrderRead, OrderDelete, \
    order_forming_complete

app_name = OrdersappConfig.name

urlpatterns = [
    path('', OrderList.as_view(), name='orders_list'),
    path('create/', OrderItemsCreate.as_view(), name='order_create'),
    path('update/<int:pk>/', OrderItemsUpdate.as_view(), name='order_update'),
    path('detail/<int:pk>/', OrderRead.as_view(), name='order_read'),
    path('delete/<int:pk>/', OrderDelete.as_view(), name='order_delete'),
    path('status/<int:pk>', order_forming_complete, name='order_forming_complete'),
]
