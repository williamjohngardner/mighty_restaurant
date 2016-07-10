from django.db import models
from django.contrib.auth.models import User


class Position(models.Model):
    position = models.CharField(max_length=15)

    def __str__(self):
        return self.position


class Profile(models.Model):
    user = models.ForeignKey('auth.User')
    position = models.ForeignKey(Position)

    def __str__(self):
        return str(self.user)


class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category


class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name


class Quantity(models.Model):
    item = models.ManyToManyField(MenuItem)
    quantity = models.IntegerField()


class Order(models.Model):
    item = models.ForeignKey(Quantity, related_name="unicorn")
    quantity = models.ForeignKey(Quantity)
    notes = models.TextField()
    profile = models.ForeignKey(Profile)

    def __str__(self):
        return str(self.pk)
