from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Distance

class DistanceListView(Listview):
    model = Distance
    template_name="thermo/thermo_list.html"

    def queryset(self):
        return Distance.objects.all()
