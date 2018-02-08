from django import forms
from .models import *
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.forms import UserCreationForm
from django.forms import HiddenInput

class RegistrationForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class ProfileForm(forms.ModelForm):
	BOOL_CHOICES = ((True, 'Male'), (False, 'Female'))
	birthdate = forms.DateField(label='Date of birth', widget=forms.SelectDateWidget(years=range(1995, 2017)))
	gender = forms.TypedChoiceField(choices=BOOL_CHOICES, widget=forms.RadioSelect(attrs=dict(required=True)),coerce=bool)

	class Meta:
		model = Profile
		fields = ('phone_number', 'birthdate', 'gender','address', 'user')

		widgets = {
            "user": HiddenInput()
        }

class AddProductForm(forms.ModelForm):
	class Meta:
		model = Product
		exclude=["id","product_seller"]

class AddBasketForm(forms.ModelForm):

	class Meta:
		model = Basket
		fields = [ 'product_id', 'basket_addition_date', 'buyer_id']

		widgets = {
            "product_id": HiddenInput(),
            "basket_addition_date": HiddenInput(),
            "buyer_id": HiddenInput()
        }















