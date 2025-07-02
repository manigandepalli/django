from .views import show, people, PersonAPI
from django.urls import path

urlpatterns = [
    path('show/', show),
    path('people', people),
    path('person', PersonAPI.as_view())
]
