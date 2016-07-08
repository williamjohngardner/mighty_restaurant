from django import forms
from app.models import Order, MenuItem, Profile

def get_choices():
    return MenuItem.objects.all().values_list("pk", "name")


def get_profiles():
    return Profile.objects.all().values_list("pk", "name")


class OrderForm(forms.ModelForm):
    item = forms.ChoiceField(choices=get_choices)
    qty = forms.FloatField()
    profile = forms.ChoiceField(choices=get_profiles)

    class Meta:
        model = Order
        fields = ["item", "qty", "notes", "profile", "fulfilled", "paid"]
