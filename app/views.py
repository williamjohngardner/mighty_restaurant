from django.shortcuts import render
from django.views.generic import TemplateView, ListView


class IndexView(TemplateView):
    template_name = "index.html"


class KitchenView(ListView):
    template_name = "index.html"


class ServerView(ListView):
    template_name = "index.html"


class OwnerView(ListView):
    template_name = "index.html"
