from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Distance

class DistanceListView(ListView):
    model = Distance
    template_name="distance/distance_list.html"

    def queryset(self):
        return Distance.objects.all()