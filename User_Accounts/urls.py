from django.urls import path
from .import views

# app_name ='User_Accounts'
urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('profile/',views.profile,name= 'profile'),
]   