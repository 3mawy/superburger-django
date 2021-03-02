from django.db import models
from django.contrib.auth.models import User, Group


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)

    class Meta:
        db_table = "customers"

    def __str__(self):
        return self.email


class Area(models.Model):
    area = models.CharField(max_length=100, null=False)

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


class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        db_table = "tasks"

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=200, null=False)

    class Meta:
        db_table = "categories"

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=100, null=False)

    class Meta:
        db_table = "sizes"

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=200)
    active = models.BooleanField(default=False, blank=True, null=True)
    score = models.DecimalField(default=1, max_digits=5, decimal_places=0)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sizes = models.ManyToManyField(Size, through='MenuItemSize')

    class Meta:
        db_table = "menu_items"

    def __str__(self):
        return self.name


class MenuItemSize(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='menu_item')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='size')
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        db_table = "menu_items_sizes"

    def __str__(self):
        return str(self.menu_item) + ' ' + str(self.size)


class Offer(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    active = models.BooleanField(default=False, blank=True, null=True)

    menu_items = models.ManyToManyField(MenuItem)

    class Meta:
        db_table = "offers"

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "status"

    def __str__(self):
        return self.name


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
