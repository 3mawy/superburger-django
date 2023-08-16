from django.db import models


class Image(models.Model):
    image = models.ImageField(null=True, blank=True)
    desc = models.CharField(null=True, blank=True, max_length=100)

    class Meta:
        db_table = "images"

    def __str__(self):
        return str(self.image)
