from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('api/products/', ProductListView.as_view(), name='product-list'),
    path('api/sellproduct/', SellproductView.as_view(), name='sell-product'),
    path('api/place-order/', PlaceOrderView.as_view(), name='place-order'),
    path('api/Vieworders/', OrderListView.as_view(), name='view-orders'),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)