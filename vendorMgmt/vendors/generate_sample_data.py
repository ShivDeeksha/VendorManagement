import random
from faker import Faker
from vendors.models import Vendor, PurchaseOrder
from django.utils import timezone

fake = Faker()

# Generate vendors with unique vendor codes
for _ in range(10):
    vendor_code = fake.unique.uuid4().split("-")[0]  # Generate a unique vendor code
    Vendor.objects.create(
        name=fake.company(),
        contact_details=fake.phone_number(),
        address=fake.address(),
        vendor_code=vendor_code
    )

# Generate purchase orders
vendors = Vendor.objects.all()
for _ in range(150):  # Create 50 purchase orders
    vendor = random.choice(vendors)
    PurchaseOrder.objects.create(
        vendor=vendor,
        po_number=fake.unique.random_number(digits=10),
        order_date=fake.date_time_this_month(),
        delivery_date=fake.date_time_this_year(),
        items={'item1': fake.word(), 'item2': fake.word()},
        quantity=random.randint(1, 100),
        status=random.choice(['pending', 'completed', 'canceled']),
        quality_rating=random.randint(1, 5),
        issue_date=fake.date_time_this_month(),
        acknowledgment_date=timezone.now() if random.random() < 0.5 else None
    )

print("Sample data generated successfully!")
