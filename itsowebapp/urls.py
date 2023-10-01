from django.urls import path
from .Login.views import Login

urlpatterns = [
    path('login/', Login.as_view()),
]
