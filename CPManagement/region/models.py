from django.db import models


class Region(models.Model):
    region = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = "Регионы"

    def __str__(self):
        return self.region
