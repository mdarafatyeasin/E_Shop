from django.urls import path
from .views import UserRegistration,UserLogin,Logout

urlpatterns = [
    path('registration/', UserRegistration, name="registration"),
    path('login/', UserLogin, name="login"),
    path('logout/', Logout, name="logout"),
    # path('profile/', UserProfile, name="profile"),
]