from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="homepage"),
    path('department',department_fun,name="deptpage"),
    path('doctors',docs_fun,name="doctorpage"),
    path('booking/',booking_fun,name="bookingpage"),
    path('about/',about,name="aboutpage"),
    path('signup/',signup,name="signuppage"),
    path('login/',user_login,name="loginpage"),
    

]