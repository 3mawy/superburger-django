from django.db import models
from django.contrib.auth.models import User, Group


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)

    class Meta:
        db_table = "customers"

    def __str__(self):
        return self.email


class Area(models.Model):
    area = models.CharField(max_length=100, null=False)
    delivery_fees = models.DecimalField(max_digits=3, decimal_places=1)

    class Meta:
        db_table = "areas"

    def __str__(self):
        return self.area


class Address(models.Model):
    area = models.ForeignKey(Area, on_delete=models.SET("deleted area"))
    address = models.CharField(max_length=200, null=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        db_table = "addresses"

    def __str__(self):
        return self.address
