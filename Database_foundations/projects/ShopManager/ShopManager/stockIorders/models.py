from django.db import models
from django.utils import timezone

class Item(models.Model):
    name = models.CharField('Please input a name', max_length=100)
    price = models.IntegerField('Please input a price', default=0)
    stock = models.IntegerField('Please input a stock amount', default=0)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.CharField('Please input customer name', max_length=100)
    date = models.DateTimeField(default=timezone.now)
    items = models.ManyToManyField(Item)

    @property
    def total_price(self):
        return sum(item.price for item in self.items.all())

    def __str__(self):
        return f"Order by {self.customer} on {self.date}"
