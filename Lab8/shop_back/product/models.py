from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField()
    is_active = models.BooleanField()

    category = models.ForeignKey(
        "category.Category", on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
