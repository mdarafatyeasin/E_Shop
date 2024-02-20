from django.urls import path
from .views import UserRegistration,UserLogin,Logout,Profile,editProfile,changePassword

urlpatterns = [
    path('registration/', UserRegistration, name="registration"),
    path('login/', UserLogin, name="login"),
    path('logout/', Logout, name="logout"),
    path('user_profile',Profile, name="user_profile"),
    path('edit_profile',editProfile, name="edit_profile"),
    path('change_password',changePassword, name="change_password"),
]