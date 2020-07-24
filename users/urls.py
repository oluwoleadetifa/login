from django.urls import path
from .views import Accessed

urlpatterns = [
    path('', Accessed.as_view()),
]
