from django.shortcuts import  render ,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from ikinciElApp.models import *
from ikinciElApp.forms import *
from django.contrib.auth import *
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.views import generic
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
import random
import requests



class HomePageView(generic.ListView):
	template_name = "home.html"
	
	def get_queryset(self):
		return Product.objects.all()

	def weather(request):
		url = 'http://api.apixu.com/v1/current.json?key=aba6dbd30810434ca8e210850161612&q=Denizli'
		req = requests.get(url)
		response = req.json()
		location=response['location']['region']
		temperature=response['current']['temp_c']
		weather_like=response['current']['condition']['text']
		result="""
			Location:{location}
			Temperature:{temperature}
			Wheather Like:{weather_like}
		""".format(location=str(location),temperature=str(temperature),weather_like=str(weather_like))
		return result

	def get_context_data(self, **kwargs):	
		context = super().get_context_data(**kwargs)
		context["productlist"] = Product.objects.all()
		context["loc"] = self.weather()
		return context


class RegistrationView(generic.FormView):
	form_class = RegistrationForm
	template_name = "signup.html"
	success_url = '/login'

	def form_valid(self, form):
		form.save()
		return super().form_valid(form)

class UserProfileView(LoginRequiredMixin ,generic.CreateView):
	form_class = ProfileForm
	template_name ="profile.html"
	success_url = '/home'

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		if self.request.method in ["POST"]:
			post_data = kwargs["data"].copy()
			user = self.request.user.id
			post_data["user"] = user
			kwargs["data"] = post_data
		return kwargs

class UserListView(LoginRequiredMixin,generic.ListView):
	template_name = "user_list.html"
	def get_queryset(self):
		return User.objects.all()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["userlist"] = User.objects.all()
		return context

class ProductView(LoginRequiredMixin,generic.ListView):
	template_name = "product_list.html"
	def get_queryset(self):
		return Product.objects.all()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["productlist"] = Product.objects.all()
		context["rand"] = random.randint(1,5)
		return context

class ProductCreateView(LoginRequiredMixin, generic.CreateView):
	form_class = AddProductForm
	template_name = "addproduct.html"
	success_url = "/productlist"

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		if self.request.method in ["POST", "PUT"]:
			post_data = kwargs["data"].copy()
			kwargs["data"] = post_data
		return kwargs

def addToBasket(request,id):
	product = Product.objects.get(id=id)
	now = timezone.now()
	buyer = User.objects.get(id = request.user.id)
	add_basket = Basket.objects.create(product_id = product,basket_addition_date = now,buyer_id = buyer)
	add_basket.save()
	profile = Profile.objects.filter(user = request.user.id)
	return HttpResponseRedirect('/productlist')

def basket_list(request):
	baskets = Basket.objects.filter(buyer_id =request.user.id)	
	return render(request, 'basket.html', {'data': baskets})

def buy_product(request,id):
	pro = Product.objects.filter(pk = id)
	pro.delete()
	return HttpResponseRedirect('/productlist')









