import uuid

from django.db import models


class Vacancy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField()
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey("Company", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
