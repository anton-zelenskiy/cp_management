from django.db import models
from region.models import Region


class Customer(models.Model):
    customer = models.CharField(max_length=70)
    region = models.ManyToManyField(Region)

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = "Заказчики"

    def __str__(self):
        return self.customer
