from django.db import models


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


class Size(models.Model):
    name = models.CharField(max_length=100, null=False)

    class Meta:
        db_table = "sizes"


class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=200)
    active = models.BooleanField(default=False, blank=True, null=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sizes = models.ManyToManyField(Size, through='MenuItemSize')

    class Meta:
        db_table = "menu_items"


class MenuItemSize(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=3)

    class Meta:
        db_table = "menu_items_sizes"


class Offer(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=3)
    active = models.BooleanField(default=False, blank=True, null=True)

    menu_items = models.ManyToManyField(MenuItem)

    class Meta:
        db_table = "offers"

