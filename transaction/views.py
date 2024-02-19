from django.shortcuts import render
from accounts.models import UserAccount

# Create your views here.
def Deposit(request):
    current_user = request.user
    print(current_user)
    user_info = UserAccount.objects.filter(user=current_user)
    print(user_info)
    return render(request, "deposit_form.html")