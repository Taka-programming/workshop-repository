from django.urls import path
from . import views
app_name = 'distance'
urlpatterns = [
path('distance_list/', views.DistanceListView.as_view(), name='distance_list'),
]
