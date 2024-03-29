from django.db import models

from users.models import User
from products.models import Product

#
#
# class BasketQuerySet(models.QuerySet):
#     def delete(self, *args, **kwargs):
#         for obj in self:
#             obj.product.quantity += obj.quantity
#             obj.product.save()
#         super(BasketQuerySet, self).delete()


class Basket(models.Model):
    # objects = BasketQuerySet.as_manager()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity

    def total_sum(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.sum() for basket in baskets)

    def total_quantity(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.quantity for basket in baskets)

    @staticmethod
    def get_items(user):
        return Basket.objects.filter(user=user)

    @staticmethod
    def get_item(pk):
        return Basket.objects.filter(pk=pk).first()

    # def delete(self):
    #     self.product.quantity += self.quantity
    #     self.product.save()
    #     super(Basket, self).delete()

    # def save(self, *args, **kwargs):
    #     if self.pk:
    #         self.product.quantity -= self.quantity - self.__class__.get_item(self.pk).quantity
    #     else:
    #         self.product.quantity -= self.quantity
    #     self.product.save()
    #     super(self.__class__, self).save(*args, **kwargs)
