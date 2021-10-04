from django.db import models
from Buyer.models import customer
from Order.models import Order
from Seller.models import Company


# Create your models here.

class Payment(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.SET_NULL,null=True,blank=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    amount = models.DecimalField(decimal_places=2,max_digits=9)
    status = models.CharField(max_length=10)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"] 

class sucessfull_Transaction(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.SET_NULL,null=True,blank=True)
    seller = models.ForeignKey(Company,on_delete=models.SET_NULL,null=True,blank=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    payment = models.ForeignKey(Payment,on_delete=models.SET_NULL,null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"] 

class unsucessfull_Transaction(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.SET_NULL,null=True,blank=True)
    seller = models.ForeignKey(Company,on_delete=models.SET_NULL,null=True,blank=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    payement = models.ForeignKey(Payment,on_delete=models.SET_NULL,null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ["-created_on"] 

    @property
    def unsucessful_Transaction(self):
        pass
