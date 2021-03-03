from django.db import models

from api.models.MenuItem import MenuItem
from api.models.Offer import Offer
from api.models.PlacedOrder import PlacedOrder


class OrderItem(models.Model):
    quantity = models.IntegerField(default=0)
    item_price = models.DecimalField(max_digits=6, decimal_places=2)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    comments = models.CharField(max_length=600)

    placed_order = models.ForeignKey(PlacedOrder, on_delete=models.CASCADE, null=False, related_name='order_items')
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, null=True, blank=True)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "order_items"

    def __str__(self):
        return 'from placed order num ' + str(self.placed_order)
