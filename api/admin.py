from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Task)
admin.site.register(models.Category)
admin.site.register(models.Size)
admin.site.register(models.MenuItem)
admin.site.register(models.Offer)
admin.site.register(models.OrderItem)
admin.site.register(models.PlacedOrder)
admin.site.register(models.Status)
