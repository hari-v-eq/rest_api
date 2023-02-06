from django.db import models

# Create your models here.


class CartItem(models.Model):
    product_id=models.ForeignKey
    product_name=models.CharField(max_length=200)
    product_price=models.FloatField()
    product_quantity=models.PositiveIntegerField()

    def __str__(self):
        return self.product_name