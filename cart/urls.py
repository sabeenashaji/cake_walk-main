
from django.urls import path
from . import views

app_name='cart'

urlpatterns = [

   path("cart/",views.cart,name="cart"),
   path('add_to_cart/<int:item_id>/',views.add_to_cart,name='add_to_cart'),
   path('view_cart/',views.view_cart,name='view_cart'),
]