from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User 
from .models import UserAccount

class UserRegistrationForm(UserCreationForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'birth_date']
    
    def save(self, commit = True):
        # commit = false because i want to save other things (behind the seen by default user balance will be added)
        our_user = super().save(commit=False)
        if commit == True:
            our_user.save()
            birth_date = self.cleaned_data.get('birth_date')

            UserAccount.objects.create(
                user = our_user,
                birth_date = birth_date,
                account_no = 100000 + our_user.id
            )
            return our_user
        
# edit user data
class edit_user_data(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
