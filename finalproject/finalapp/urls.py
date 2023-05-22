from django.urls import path
from finalapp import views

urlpatterns = [
    path("",views.Home,name='home'),
    path("register/",views.Register, name="register"),
    path("data/",views.Data,name="data"),
    path("clear/<int:id>/",views.Delete,name="clear"),
    path("edit/<int:id>/",views.Update,name="edit"),
    path("signup/",views.SignUp, name="signup"),
    path("logged/",views.Logged,name="logged"),
    path('loggedout/',views.Log_Out,name='loggedout')
]