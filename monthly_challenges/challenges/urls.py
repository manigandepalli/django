from django.urls import path
from .import views
urlpatterns = [
    path("<int:month>", views.month_challenge_by_number),
    path("<str:month>", views.monthly_challenges, name="month-challenge")
]
