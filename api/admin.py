from django.contrib import admin
from api import models

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
admin.site.register(models.Image)
admin.site.register(models.CarouselImage)
admin.site.register(models.Extra)
admin.site.register(models.Cart)
admin.site.register(models.CartItem)
