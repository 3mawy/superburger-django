from django.contrib import admin
from .models import models

# Register your models here.

admin.site.register(models.Category)
admin.site.register(models.Size)
admin.site.register(models.MenuItem)
admin.site.register(models.Offer)
admin.site.register(models.OrderItem)
admin.site.register(models.PlacedOrder)
admin.site.register(models.Status)
admin.site.register(models.MenuItemSize)
admin.site.register(models.Customer)
admin.site.register(models.Area)
admin.site.register(models.Address)
