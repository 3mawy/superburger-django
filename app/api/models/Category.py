from django.db import models

from api.models import Image


class Category(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=200, null=False)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    class Meta:
        db_table = "categories"

    def __str__(self):
        return self.name
