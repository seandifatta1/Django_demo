from django.urls import path
from .views import see_results

urlpatterns = [
    path('results/', see_results, name='results'),
]
