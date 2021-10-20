from django.shortcuts import render

# Create your views here.
def Organic(response):
	return render(response,"YS/index.html",{})

def CONTACT(response):
	return render(response,"YS/contact.html",{})

def Checkout(response):
	return render(response,"YS/checkout.html",{})

def Shopdetails(response):
	return render(response,"YS/shop-details.html",{})

def Shop(response):
	return render(response,"YS/shop-grid.html",{})

def ShoppingCart(response):
	return render(response,"YS/shoping-cart.html",{})

