from django.db import models
from Buyer.models import customer
from Product.models import Product

# Create your models here.

class ProductCart(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.product.product_name

        

    def get_total_product_price(self):
        return self.quantity * self.product.price


class Order(models.Model):
    ORDER_STATUS = (
    ('placed', 'Placed'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
    ('cancelled','Cancelled'))
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    product = models.ManyToManyField(ProductCart)
    address = models.CharField(max_length=250)
    address_second = models.CharField(max_length=250, null=True, blank=True)
    postal_code = models.CharField(max_length=6)
    country = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100)
    ordered_date = models.DateField(auto_now=True)
    status = models.CharField(max_length=120,choices=ORDER_STATUS,default='created')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return str(self.id)


    class Meta:
        ordering = ["-ordered_date"]    

    @property
    def get_total_price(self):
        total = 0
        for product in self.product.all():
            total = total + product.get_total_product_price()
        return total


    def is_completed(self):
        return True if self.status == "paid" else False    
