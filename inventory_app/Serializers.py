from rest_framework import serializers

from inventory_app.models import Inventory


class InventorySerializer(serializers.ModelSerializer):
    supplier = serializers.SerializerMethodField()

    def get_supplier(self, obj):
        return obj.supplier.name

    class Meta:
        model = Inventory
        fields = ['name', 'availability', 'supplier']

