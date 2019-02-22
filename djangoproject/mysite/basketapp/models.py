from django.db import models
from django.conf import settings
from mainapp.models import CollectionsImg

class Basket(models.Model):
    basket_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='user')
    basket_product = models.ForeignKey(CollectionsImg, on_delete=models.CASCADE, verbose_name='product')
    basket_quantity = models.PositiveIntegerField(verbose_name='quantity', default=0)
    basket_datetime = models.DateTimeField(verbose_name='time_of_addition', auto_now_add=True)

    def __str__(self):
        return str(self.basket_user)

    def _get_product_cost(self):
        return self.basket_product.img_collection.collection_price * self.basket_quantity

    product_cost = property(_get_product_cost)

    def _get_total_quantity(self):
        _items = Basket.objects.filter(basket_user=self.basket_user)
        _totalquantity = sum(list(map(lambda x: x.basket_quantity, _items)))
        return _totalquantity

    total_quantity = property(_get_total_quantity)

    def _get_total_cost(self):
        _items = Basket.objects.filter(basket_user=self.basket_user)
        _totalcost = sum(list(map(lambda x: x.product_cost, _items)))
        return _totalcost

    total_cost = property(_get_total_cost)