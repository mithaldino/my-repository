from django import forms
from iphoneapp.models import *


class Adminform(forms.ModelForm):
    class Meta:
        model = Admins
        fields = '__all__'
		
class Customerform(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        
class Storeform(forms.ModelForm):
    class Meta:
        model = Store
        fields = '__all__'
        
class Cartform(forms.ModelForm):
    class Meta:
        model = Cart
        fields = '__all__'
        
class Orderform(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'