from django.shortcuts import render, redirect
from .models import shop_model
from products.models import Product
from transaction.models import userTransaction
from accounts.models import UserAccount
from decimal import Decimal
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
from django.template.loader import render_to_string

# email
def send_transaction_email(user, amount, subject, template):
        message = render_to_string(template, {
            'user' : user,
            'amount' : amount,
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()

def byNow(request, id):
    user = request.user
    product_id = id
    product = Product.objects.get(pk=product_id)

    # Ensure the user has enough balance to make the purchase
    if user.account.balance >= Decimal(product.price):
        if int(product.quantity) > 0:
            # Deduct the product price from the user's balance
            user.account.balance -= Decimal(product.price)
            user.account.save()

            # Create a transaction record
            userTransaction.objects.create(
                user=user,
                transaction_type='buy books',
                amount=Decimal(product.price)
            )

            # Update product quantity
            product.quantity = int(product.quantity) - 1
            product.save()

            # Create shop model record
            purchase = shop_model.objects.create(author_name=user, product_id=product_id)
            messages.success(
                request,f'{"{:,.2f}".format(float(product.price))}$ was cut from your account successfully'
            )
            send_transaction_email(request.user, product.price, "Parches Message", "parches_email.html")
            return redirect("product_details", id=product_id)
        else:
            messages.warning(request, "The product is out of stock")
            return redirect("home")
    else:
        # Handle cases where the user does not have enough balance or the product is out of stock
        messages.warning(request, "Insufficient balance please deposit")
        return redirect("deposit")
