from django.urls import path
from .views import (
    PersonAdd,
    GetPerson,
    TestTemplate,
    TopicApi
)

urlpatterns = [
    path('person_add/', PersonAdd),
    path('getuser/<str:pk>/', GetPerson),
    path('test_template/', TestTemplate.as_view()),
    path('topic/', TopicApi.as_view()),
]