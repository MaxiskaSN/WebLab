from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('login', views.loginPage, name="loginPage"),
    path('register', views.register, name="register"),
    path('logout', views.logoutUser, name="logout"),
    path('feedback', views.feedback, name="feedback"),
    path('profile', views.profile, name="profile"),
]
