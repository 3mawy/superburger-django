from django.db import models

from api.models.Category import Category
from api.models.Image import Image


class Size(models.Model):
    name = models.CharField(max_length=100, null=False)
    name_ar = models.CharField(max_length=200)

    class Meta:
        db_table = "sizes"

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    name_ar = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    description_ar = models.CharField(max_length=200)
    active = models.BooleanField(default=False, blank=True, null=True)
    score = models.DecimalField(default=1, max_digits=5, decimal_places=0)

    image = models.ForeignKey(Image, on_delete=models.CASCADE)
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
