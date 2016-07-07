from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView

from app.models import Category, MenuItem, Profile, Position, Order


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
        return context


class OwnerView(ListView):
    template_name = "owner.html"
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context
