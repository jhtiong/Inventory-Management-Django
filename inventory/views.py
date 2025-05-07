from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Inventory
from .serializers import InventorySerializer

# Create your views here.

class InventoryListAPIView(ListAPIView):
    queryset = Inventory.objects.select_related('supplier').all()
    serializer_class = InventorySerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

class InventoryDetailAPIView(RetrieveAPIView):
    queryset = Inventory.objects.select_related('supplier').all()
    serializer_class = InventorySerializer

def inventory_list(request):
    # Get the search query from URL parameters
    search_query = request.GET.get('name', '')
    
    # Filter queryset if search query exists
    queryset = Inventory.objects.select_related('supplier').all()
    if search_query:
        queryset = queryset.filter(name__icontains=search_query)
    
    return render(request, 'inventory/list.html', {'inventories': queryset})

def inventory_detail(request, pk):
    inventory = get_object_or_404(Inventory.objects.select_related('supplier'), pk=pk)
    return render(request, 'inventory/detail.html', {'inventory': inventory})
