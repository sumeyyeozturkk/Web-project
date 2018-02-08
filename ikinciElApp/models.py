from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
	category_name = models.CharField(max_length = 50)

	def __str__(self):
		return self.category_name

class Brand(models.Model):
	brand_name = models.CharField(max_length = 50)

	def __str__(self):
		return self.brand_name

class Product(models.Model):
	product_name = models.CharField(max_length = 50)
	product_price =models.DecimalField(max_digits=6, decimal_places=2)
	product_picture = models.ImageField(upload_to='static/images/',blank = True)
	product_brand = models.ForeignKey(Brand, on_delete =models.PROTECT)
	product_category = models.ForeignKey(Category, on_delete = models.PROTECT)
	product_seller = models.ForeignKey(User,on_delete= models.PROTECT,default = 1)

	def __str__(self):
		return str(self.id)

		
class Basket(models.Model):
	product_id = models.ForeignKey(Product, on_delete = models.CASCADE)
	basket_addition_date =models.DateTimeField(null = True, blank=True)
	buyer_id = models.ForeignKey(User,on_delete=models.PROTECT)
	
	def __str__(self):
		return str(self.id)
	
	def BasketSumProduct():
		total = Basket.objects.filter('buyer_id').Count()
		return total

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True, related_name = 'profile')
	phone_number = models.CharField(max_length=11)
	birthdate = models.DateField(null=True, blank=True)
	BOOL_CHOICES = ((True, 'Male'), (False, 'Female'))
	gender = models.NullBooleanField(choices=BOOL_CHOICES, blank=True, null=True)
	address = models.TextField()
	
	def __str__(self):
		return self.user.username


