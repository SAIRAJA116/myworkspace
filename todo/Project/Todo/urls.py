from django.urls import path
from . import views

urlpatterns=[

    path("",views.home,name="home"),
    path("add/",views.addTask,name="add"),
    path("delete/<int:id>",views.delete,name="delete"),
    path("login/",views.loginpage,name="login"),
    path("register/",views.registerpage,name="register"),
    path("logout/",views.logoutpage,name="logout")
]
