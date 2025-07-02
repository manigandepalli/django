from .views import show, people, PersonAPI, PeopleViewset
from django.urls import path, include
from rest_framework.routers import DefaultRouter


##to register APIview we use .as_view()
##to register ModelViewset we use routers

router = DefaultRouter()
router.register(r'people', PeopleViewset, basename='people')
urlpatterns = [
    path('show/', show),
    path('people', people),
    path('person', PersonAPI.as_view()),
    path('', include(router.urls))
]
