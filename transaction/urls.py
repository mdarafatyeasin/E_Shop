from django.urls import path
from .views import Deposit

urlpatterns = [
    path("add_balance", Deposit, name="deposit"),
]