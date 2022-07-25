from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField("Категорія", max_length=150)
    description = models.TextField("Опис", blank=True)
    slug = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"
