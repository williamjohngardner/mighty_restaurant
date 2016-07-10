from django import forms
from django.forms import inlineformset_factory

from app.models import Order, MenuItem, Profile, Quantity


def get_choices():
    return MenuItem.objects.all().values_list("pk", "name")

def get_profiles():
    return Profile.objects.all().values_list("pk", "name")

def get_quantity():
    return Quantity.objects.all().values_list("pk", "quantity")


class OrderForm(forms.ModelForm):
    item = forms.ChoiceField(choices=get_choices)
    # quantity = forms.ChoiceField(choices=get_quantity)
    # profile = forms.ChoiceField(choices=get_profiles)

    class Meta:
        model = Quantity
        fields = ["item", "quantity"]
