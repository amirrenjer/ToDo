from django.contrib import admin
from django.urls import path
from .views import Login_view, signup_view, Logout_view
app_name = 'accounts'
urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', Login_view, name='login'), 
    path('logout/', Logout_view, name='logout'),

]