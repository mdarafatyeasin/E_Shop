from django.urls import path
from .views import Deposit,TransactionHistory

urlpatterns = [
    path("add_balance", Deposit, name="deposit"),
    path("transaction_history", TransactionHistory, name="transaction_history"),
]