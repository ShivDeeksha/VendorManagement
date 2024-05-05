from rest_framework import generics
from django.db.models import Avg, Count
from django.db.models.functions import Coalesce
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer
from rest_framework.response import Response
from django.db import models
from rest_framework.permissions import IsAdminUser



class VendorListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        vendor_id = self.request.query_params.get('vendor')
        if vendor_id:
            queryset = queryset.filter(vendor=vendor_id)
        return queryset

class PurchaseOrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class VendorPerformanceAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAdminUser]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def get(self, request, *args, **kwargs):
        vendor_id = self.kwargs.get('vendor_id')
        metrics = calculate_vendor_metrics(vendor_id)
        return Response(metrics)

def calculate_vendor_metrics(vendor_id):
    vendor = Vendor.objects.get(id=vendor_id)

    # Calculate on-time delivery rate
    completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
    total_completed_orders = completed_orders.count()
    on_time_delivery_rate = (completed_orders.filter(delivery_date__lte=models.F('delivery_date')).count() * 100) / (total_completed_orders or 1)

    # Calculate quality rating average
    quality_rating_avg = completed_orders.aggregate(avg_quality=Avg('quality_rating'))['avg_quality'] or 0

    # Calculate average response time
    response_time_avg = completed_orders.aggregate(avg_response=Avg(models.F('acknowledgment_date') - models.F('issue_date')))['avg_response'] or 0

    # Convert CombinedExpression object to float
    response_time_avg = response_time_avg.total_seconds() if response_time_avg else 0

    # Calculate fulfillment rate
    total_orders = PurchaseOrder.objects.filter(vendor=vendor).count()
    fulfillment_rate = (completed_orders.count() * 100) / (total_orders or 1)

    return {
        'on_time_delivery_rate': on_time_delivery_rate,
        'quality_rating_avg': quality_rating_avg,
        'average_response_time': response_time_avg,
        'fulfillment_rate': fulfillment_rate
    }
