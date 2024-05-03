from django import forms
from .models import Order

<<<<<<< HEAD


class OrderForm(forms.ModelForm):
     class Meta:
          model = Order
          fields = ('name','email','phone','address','district', 'payment')
=======
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'email', 'phone', 'address', 'district', 'payment')
>>>>>>> ef72134baa270a2b0a06d1d92d996e14e6d57652

