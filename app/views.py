from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from app.models import Category, Menu


class IndexView(TemplateView):
    template_name = "index.html"


class KitchenView(ListView):
    template_name = "kitchen.html"
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context

class ServerView(ListView):
    template_name = "index.html"


class OwnerView(ListView):
    template_name = "index.html"
