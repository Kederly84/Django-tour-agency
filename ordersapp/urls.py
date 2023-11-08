from django.urls import path

from ordersapp.apps import OrdersappConfig
from ordersapp.views import OrderList, OrderItemsCreate, OrderItemsUpdate, OrderRead

app_name = OrdersappConfig.name

urlpatterns = [
    path('', OrderList.as_view(), name='order_list'),
    path('create/', OrderItemsCreate.as_view(), name='order_create'),
    path('update/<int:pk>/', OrderItemsUpdate.as_view(), name='order_update'),
    path('detail/<int:pk>/', OrderRead.as_view(), name='order_read'),
]
