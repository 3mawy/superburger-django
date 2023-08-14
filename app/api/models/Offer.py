from django.db import models

from api.models import Image
from api.models.MenuItem import MenuItem


class Offer(models.Model):
    name = models.CharField(max_length=200)
    name_ar = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    description_ar = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    active = models.BooleanField(default=False, blank=True, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    max_offer_items = models.IntegerField()

    menu_items = models.ManyToManyField(MenuItem)

    class Meta:
        db_table = "offers"

    def __str__(self):
        return self.name
