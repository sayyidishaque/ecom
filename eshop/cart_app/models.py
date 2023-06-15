from django.db import models
from shop_app.models import Products


# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'cart'
        ordering = ['date_added',]

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quandity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'CartItem'

    def subtotal(self):
        return '{}'.format(self.product.price * self.quandity)

    def __str__(self):
        return '{}'.format(self.product)
