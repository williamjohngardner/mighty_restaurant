from django import forms
from django.forms import inlineformset_factory

from app.models import Order, MenuItem, Profile, Quantity


def get_choices():
    return MenuItem.objects.all().values_list("pk", "name")

def get_profiles():
    return Profile.objects.all().values_list("pk", "name")

def get_order():
    return Order.objects.all().values_list("pk", "name")


class OrderNumber(forms.ModelForm):
    profile = forms.ChoiceField(choices=get_profiles)

    class Meta:
        model = Order
        fields = ["profile"]


class OrderForm(forms.ModelForm):
    order_items = forms.ChoiceField(choices=get_choices)
    order = forms.ChoiceField(choices=get_order)


    class Meta:
        model = Quantity
        fields = ["order_items", "quantity", "notes", "order"]
