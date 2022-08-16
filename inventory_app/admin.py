from django.contrib import admin

from inventory_app.models import Inventory, Supplier


admin.site.register(Inventory)
admin.site.register(Supplier)
