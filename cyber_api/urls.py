from django.urls import path
from .views import (
    PersonAdd,
)

urlpatterns = [
    path('person_add/', PersonAdd),
]