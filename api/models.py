from django.db import models
from django.contrib.auth.models import User, Group


# Create your models here.

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

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sizes = models.ManyToManyField(Size, through='MenuItemSize')

    class Meta:
        db_table = "menu_items"

    def __str__(self):
        return self.name


class MenuItemSize(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=3)

    class Meta:
        db_table = "menu_items_sizes"

    def __str__(self):
        return str(self.menu_item) + ' ' + str(self.size)


class Offer(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=3)
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
    estimated_delivery_time = models.TimeField(auto_now=False)
    delivery_address = models.CharField(max_length=600)
    delivery_notes = models.CharField(max_length=600)
    total_price = models.DecimalField(max_digits=8, decimal_places=3)
    user = models.ManyToManyField(User)
    status = models.ManyToManyField(Status, through='OrderStatus')

    class Meta:
        db_table = "placed_orders"

    def __str__(self):
        return str(self.id)


class OrderStatus(models.Model):
    timestamp = models.TimeField(auto_now=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=False)
    placed_order = models.ForeignKey(PlacedOrder, on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = "order_status"


class OrderItem(models.Model):
    quantity = models.IntegerField()
    item_price = models.DecimalField(max_digits=6, decimal_places=3)
    total_price = models.DecimalField(max_digits=8, decimal_places=3)
    comments = models.CharField(max_length=600)

    placed_order = models.ForeignKey(PlacedOrder, on_delete=models.CASCADE, null=False)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "order_items"

    def __str__(self):
        return 'from placed order num ' + str(self.placed_order)

