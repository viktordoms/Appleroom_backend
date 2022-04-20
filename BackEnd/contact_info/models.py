from django.db import models

# Create your models here.
class Number(models.Model):
    number = models.CharField("Номер", max_length=50)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = "Номер"
        verbose_name_plural = "Номери"


class City(models.Model):
    title = models.CharField("Місто", max_length=50)
    slug = models.SlugField(max_length=160, unique=True)
    numbers = models.ManyToManyField(
        Number, verbose_name="Номер"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Місто"
        verbose_name_plural = "Міста"
