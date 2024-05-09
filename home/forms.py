from django import forms
from .models import Order
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'email', 'phone', 'address', 'district', 'payment')


    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError("Ism noto'g'ri formatda kiritildi!!!")
        return name

    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email kiritilishi shart.")
        return email


    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone:
            raise forms.ValidationError("Telefon nomer kiritilishi shart!")
        return phone
    

    def clean_address(self):
        address = self.cleaned_data.get('address')
        if not address:
            raise forms.ValidationError('Maydonlar bo\' bo\'lmasligi lozim.')
        return address

    
    def clean_district(self):
        district = self.cleaned_data.get('district')
        if not district:
            raise forms.ValidationError('Maydonlar bo\' bo\'lmasligi lozim.')
        return district


    def clean_payment(self):
        payment = self.cleaned_data.get('payment')
        if not payment:
            raise forms.ValidationError('Maydonlar bo\' bo\'lmasligi lozim.')
        return payment
