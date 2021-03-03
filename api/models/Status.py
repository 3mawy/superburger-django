from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "status"

    def __str__(self):
        return self.name
