from .views import show, people
from django.urls import path

urlpatterns = [
    path('show/', show),
    path('people', people)
]
