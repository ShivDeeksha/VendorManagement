from rest_framework import serializers
from .models import Vendor,PurchaseOrder

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        exclude = ['vendor_code']

    def create(self, validated_data):
        vendor = Vendor.objects.create_vendor(**validated_data)
        return vendor

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['vendor_code'] = instance.vendor_code
        return rep

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'