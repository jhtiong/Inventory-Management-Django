from django.contrib import admin
from .models import Supplier, Inventory

# Register your models here.
admin.site.register(Supplier)
admin.site.register(Inventory)
