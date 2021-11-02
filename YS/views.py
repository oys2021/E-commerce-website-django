from django.core.checks import messages
from django.http import response
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Product
# Create your views here.
def Organic(response):
	return render(response,"YS/index.html",{})

def CONTACT(response):
	return render(response,"YS/contact.html",{})

def Checkout(response):
	return render(response,"YS/checkout.html",{})


def Shop(response):
	products=Product.objects.all()
	return render(response,"YS/shop-grid.html",{'products':products})

def Shopdetails(response):
	return render(response,"YS/shop-details.html",{})


def ShoppingCart(response):
	return render(response,"YS/shoping-cart.html",{})

def Login(response):
	if response.method=="POST":
		username=response.POST["user"]
		password=response.POST["password_1"]

		user=auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(response,user)
			return redirect("/organic")
		else:
			messages.info(response,"Invalid credentials")
			return redirect("/login")
	
	else:
		return render(response,"YS/login.html",{})


def Signup(response):
	if response.method=="POST":
		first_name=response.POST["first"]
		last_name=response.POST["last"]
		username=response.POST["user"]
		password1=response.POST["password_1"]
		passw2=response.POST["password_2"]
		email=response.POST["email"]

		if password1==passw2:
			user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
			user.save()
			print("Good to go")
			return redirect("/login")
		
		else:
			print("Error")

	else:
		return render(response,"YS/signup.html",{})

			

        
			
			

		
		

	

		

	


