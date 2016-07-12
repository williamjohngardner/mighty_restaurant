from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView
from django.http import HttpResponseRedirect

from app.models import Category, MenuItem, Profile, Position, Order, Quantity
from app.forms import OrderForm, OrderNumber


class IndexView(TemplateView):
    template_name = "index.html"


class CreateUserView(CreateView):
    model = Profile
    form_class = UserCreationForm
    success_url = "/login"


class ProfilePageView(UpdateView):
    fields = ["user", "position"]
    model = Profile
    success_url = reverse_lazy("index_view")

    def get_object(self, queryset=None):
        return self.request.user


class KitchenView(ListView):
    template_name = "kitchen.html"
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context

class ServerView(ListView):
    template_name = "server.html"
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['menu_items_list'] = MenuItem.objects.all()
        return context


class OrderListView(ListView):
    template_name = "order_list.html"
    model = Order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_list'] = Order.objects.all()
        return context


class OrderDetailView(DetailView):
    model = Order


class CreateOrderNumber(CreateView):
    form = OrderNumber
    fields = ["profile"]
    success_url = reverse_lazy("create_order_view")
    queryset = Order.objects.all()
    template_name = "app/order_form.html"


class CreateOrderView(CreateView):
    form = OrderForm
    fields = ["order_items", "quantity", "notes", "order"]
    success_url = reverse_lazy("create_order_view")
    queryset = Quantity.objects.all()
    template_name = "app/order_form.html"


class DisplayOrderView(ListView):
    template_name = "order.html"
    model = Quantity

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_items'] = Order.objects.all()
        # context['qty_items'] = Quantity.objects.all()
        return context


class OwnerView(ListView):
    template_name = "owner.html"
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['menu_items_list'] = MenuItem.objects.all()
        return context
