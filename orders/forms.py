from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['last_name', 'first_name', 'surname', 'mobile', 'email']
