from django.db import models


class Cart(models.Model):
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    class Meta:
        db_table = "carts"

    def __str__(self):
        return 'user' + str(self.customer.id) + 'cart'
