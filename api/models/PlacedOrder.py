from django.db import models

from api.models.Customer import Customer
from api.models.Customer import Address
from api.models.Status import Status


class PlacedOrder(models.Model):
    order_time = models.TimeField(auto_now=True)
    estimated_delivery_time = models.TimeField(auto_now=False, null=True)
    delivery = models.BooleanField(default=False, null=False)
    delivery_address = models.ForeignKey(Address, on_delete=models.SET('deleted address'))
    delivery_notes = models.CharField(max_length=600, null=True, blank=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    customer = models.ForeignKey(Customer, on_delete=models.SET('deleted customer'))
    status = models.ForeignKey(Status, on_delete=models.SET('deleted status'))
    complete = models.BooleanField(default=False)

    class Meta:
        db_table = "placed_orders"

    def __str__(self):
        return str(self.id)
