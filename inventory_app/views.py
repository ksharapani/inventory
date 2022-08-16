from rest_framework import generics, status
from rest_framework.response import Response
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from inventory_app.Serializers import InventorySerializer
from inventory_app.models import Inventory


class InventoryView(ListView):
    # specify the model for list view
    model = Inventory
    template_name = 'inventory_app/inventory_list.html'

    def get_queryset(self, *args, **kwargs):
        qs = super(InventoryView, self).get_queryset()
        name = self.request.GET.get('name', None)
        if name:
            qs = qs.filter(name__contains=name)
        return qs


class InventoryDetailView(DetailView):
    # specify the model for list view
    model = Inventory
    template_name = 'inventory_app/inventory_detail.html'


class InventoryAPIView(generics.ListAPIView):
    serializer_class = InventorySerializer

    def get_queryset(self):
        return Inventory.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'status': 1, 'message': 'Data retrieved successfully', 'result': serializer.data},
                        status=status.HTTP_200_OK)

