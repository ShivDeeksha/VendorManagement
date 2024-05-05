from django.contrib import admin
from .models import Vendor, PurchaseOrder

class PurchaseOrderInline(admin.TabularInline):
    model = PurchaseOrder
    extra = 0

class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_details', 'address', 'vendor_code')
    inlines = [PurchaseOrderInline]  # Add PurchaseOrderInline to show related purchase orders

admin.site.register(Vendor, VendorAdmin)