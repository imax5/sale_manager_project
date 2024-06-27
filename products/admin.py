from django.contrib import admin

from .models import Product, ProductWarehouse, Unit, Warehouse

admin.site.register(Product)
admin.site.register(ProductWarehouse)
admin.site.register(Unit)
admin.site.register(Warehouse)
