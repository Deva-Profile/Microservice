from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import  *
from .models import *


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()  
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class SellproductView(APIView):
    def post(self, request):
        data = request.data
        try:
            product = Product.objects.create(
                name=data['name'],
                description=data['description'],
                price=data['price'],
                image =data['image'],
                phone_number=data['phone_number'],
                
            )
            ProductSerializer = SellproductSerializer(product)
            return Response({'message': 'Product sold successfully', "redirect_to": "/home"},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

class PlaceOrderView(APIView):
    def post(self, request):
        data = request.data
        product = data.get('product')
        try:
            product = Product.objects.get(name__iexact=product)
            if not product.available:
                return Response(
                    {"error": "This product is not available."},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Product.DoesNotExist:
            return Response(
                {"error": "Product not found."},
                status=status.HTTP_404_NOT_FOUND
            )   
        
        data['product'] = product.id
        serializer = OrderViewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Order created successfully",
                "redirect_to": "/home"
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class OrderListView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderViewSerializer(orders, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)