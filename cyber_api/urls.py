from django.urls import path
from .views import (
    PersonAdd,
    GetPerson,
    TestTemplate
)

urlpatterns = [
    path('person_add/', PersonAdd),
    path('getuser/<str:pk>/', GetPerson),
    path('test_template/', TestTemplate.as_view())
]