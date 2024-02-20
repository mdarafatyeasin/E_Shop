from django.shortcuts import render, redirect
from accounts.models import UserAccount
from .forms import DepositForm
from .models import userTransaction
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages

# email 
def send_transaction_email(user, amount, subject, template):
        message = render_to_string(template, {
            'user' : user,
            'amount' : amount,
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()

# deposit
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
                messages.success(
                     request,f'{"{:,.2f}".format(float(amount))}$ was deposited to your account successfully'
                )
                send_transaction_email(request.user, amount, "Deposite Message", "deposit_email.html")
                return redirect('home')  # Redirect to a success URL
            else:
                pass
    return render(request, "deposit_form.html", {"form": add_balance_form})

# Transaction History
def TransactionHistory(request):
     user_history = userTransaction.objects.filter(user = request.user)
     print(user_history)
     return render(request, "transaction_history.html", {"user_history":user_history})

