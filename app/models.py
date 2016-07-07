from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category


class Menu(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(Category)
    photo = models.ImageField(upload_to="menu_photos", null=True, blank=True, verbose_name="Menu Photo")

    def __str__(self):
        return self.name
