from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *



class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [ 'name', 'price', 'image', 'available', 'description']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None
    

class SellproductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'phone_number']


class OrderViewSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True)  
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_price = serializers.DecimalField(source='product.price', max_digits=10, decimal_places=2, read_only=True)
    product_image = serializers.SerializerMethodField()  

    class Meta:
        model = Order
        fields = [
            'product', 'product_name', 'product_price', 'product_image',
            'buyer_name', 'buyer_contact', 'quantity', 'payment_option'
        ]
        extra_kwargs = {
            'product': {'write_only': True}  
        }

    def get_product_image(self, obj):
        request = self.context.get('request')
        if obj.product.image:
            if request:
                return request.build_absolute_uri(obj.product.image.url)
            else:
                return obj.product.image.url  
        return None 