from django.contrib import admin
from .models import Payment,sucessfull_Transaction,unsucessfull_Transaction
# Register your models here.


admin.site.register(Payment)


admin.site.register(sucessfull_Transaction)

admin.site.register(unsucessfull_Transaction)