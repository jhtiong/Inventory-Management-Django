from rest_framework import serializers
from .models import Supplier, Inventory

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name']

class InventorySerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(read_only=True)

    class Meta:
        model = Inventory
        fields = ['id', 'name', 'description', 'note', 'stock', 'availability', 'supplier'] 