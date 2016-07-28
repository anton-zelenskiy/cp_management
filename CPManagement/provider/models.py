from django.db import models
from region.models import Region


class Provider(models.Model):
    provider = models.CharField(max_length=70)
    region = models.ManyToManyField(Region)

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = "Поставщики"

    def __str__(self):
        return self.provider
