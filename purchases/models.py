from django.db import models
from gifts.models import Gift
import uuid

class Purchase(models.Model):

    name = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)
    emails = models.EmailField(max_length=128, null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)
    address_line1 = models.CharField(max_length=100, null=False, blank=False)
    address_line2 = models.CharField(max_length=100, null=False, blank=True)
    address_line3 = models.CharField(max_length=100, null=True, blank=True)
    town = models.CharField(max_length=100, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=20, null=False, blank=False)
    order_number = models.CharField(max_length=16, null=False, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=7, decimal_places=2, null=False, default=0)

class LineItem (models.Model):
    purchase = models.ForeignKey(Purchase, null=False, blank=False, on_delete=models.CASCADE)
    gift = models.ForeignKey(Gift, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    total = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False, editable=False)

    def create_order_number(self):
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):

        if not self.order_number:
            self.order_number = self.create_order_number()
        super().save(*args, **kwargs)