from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=128)
    species = models.CharField(max_length=128)
    breed = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)


class Pizza(models.Model):
    name = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)


class Topping(models.Model):
    name = models.CharField(max_length=128)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


"""
Topping.objects.get(1).pizza


pizza = Pizza.objects.get(1)
pizza.topping_set.all()
"""
