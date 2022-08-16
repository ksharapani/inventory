from django.urls import path

from inventory_app.views import InventoryView, InventoryDetailView, InventoryAPIView

urlpatterns = [
    path("inventory", InventoryView.as_view(), name="inventory"),
    path("inventory/<pk>", InventoryDetailView.as_view(), name="inventory_detail"),
    path("api/inventory", InventoryAPIView.as_view(), name="inventory_api"),
]
