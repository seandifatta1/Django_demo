from django.urls import path
from .views import see_results

urlpatterns = [
    path('see_results/', see_results, name='see_results'),
]
