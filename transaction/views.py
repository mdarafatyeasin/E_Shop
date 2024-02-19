from django.shortcuts import render, redirect
from accounts.models import UserAccount
from .forms import DepositForm
from .models import userTransaction

def Deposit(request): 
    add_balance_form = DepositForm(request.POST or None)
    if request.method == "POST":
        if add_balance_form.is_valid():
            amount = add_balance_form.cleaned_data['amount']
            current_user = request.user
            user_info = UserAccount.objects.filter(user=current_user).first()
            if user_info:
                old_balance = user_info.balance
                new_balance = old_balance + amount
                user_info.balance = new_balance
                user_info.save()
                # Create a new transaction record
                userTransaction.objects.create(user=current_user, transaction_type='deposit', amount=amount)
                return redirect('home')  # Redirect to a success URL
            else:
                pass
    return render(request, "deposit_form.html", {"form": add_balance_form})
