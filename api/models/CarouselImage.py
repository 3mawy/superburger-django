from django.db import models

from api.models import Image


class CarouselImage(models.Model):
    description = models.CharField(max_length=200, null=True, blank=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    class Meta:
        db_table = "carousel_image"

    def __str__(self):
        return self.description
