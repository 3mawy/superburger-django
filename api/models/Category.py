from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=200, null=False)

    class Meta:
        db_table = "categories"

    def __str__(self):
        return self.name
