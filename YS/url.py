from django.urls import path
from .import views


urlpatterns=[
path("organic",views.Organic,name="organic"),
path("CONTACTS",views.CONTACT,name="cont"),
path("Checkout",views.Checkout,name="check"),
path("Shopdetails",views.Shopdetails,name="shopd"),
path("Shop",views.Shop,name="Shop"),
path("ShoppingCart",views.ShoppingCart,name="cart"),


]