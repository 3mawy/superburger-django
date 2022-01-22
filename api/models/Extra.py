from django.db import models


class Extra(models.Model):
    name = models.CharField(max_length=100, null=False)
    name_ar = models.CharField(max_length=100, null=False)
    price = models.DecimalField(max_digits=4, decimal_places=1)

    class Meta:
        db_table = "extras"

    def __str__(self):
        return self.name
