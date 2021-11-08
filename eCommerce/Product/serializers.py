
from rest_framework import serializers


from .models import Product,Category



class ProductSerializer(serializers.ModelSerializer):
   class Meta:
        model = Product
        fields = ('id','product_name','product_code','category','product_dimension','price','stock','is_active','seller','employee')
   
    
              
   
   def validate_product_dimension(self,value):
        if value['not_valid']:
            raise serializers.ValidationError("Not valid")
        return value  

  



class CategorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True)
    class Meta:
        model=Category
        fields = ('id','name','description','product')




