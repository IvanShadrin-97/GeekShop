from django.db import models

from users.models import User
from products.models import Products


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} |  Продукт для {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price

    def total_price(self):
        baskets = Basket.objects.filter(user=self.user)
        for basket in baskets:
            sum(basket.sum())
        return baskets

    def total_quantity(self):
        baskets = Basket.objects.filter(user=self.user)
        for basket in baskets:
            sum(basket.quantity)
        return baskets