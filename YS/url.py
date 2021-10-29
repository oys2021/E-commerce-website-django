from django.urls import path
from .import views


urlpatterns=[
path("organic",views.Organic,name="organic"),
path("CONTACTS",views.CONTACT,name="contact"),
path("Shop",views.Shop,name="Shop"),
path("Shopd",views.Shopdetails,name="shopd"),
path("Shopart",views.ShoppingCart,name="cart"),
path("checkout",views.Checkout,name="check"),
path("cont",views.CONTACT,name="cont"),

]