from django.shortcuts import render
from django.views.generic import TemplateView

class restaurantView(TemplateView):
    template_name = 'restaurant/pages/'
