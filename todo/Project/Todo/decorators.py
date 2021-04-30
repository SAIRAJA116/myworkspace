from django.http import HttpResponse
from django.shortcuts import redirect


#I wrote all these code by seeing the lectures on youtube Django 3.0 crashcourse IVEY


def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if(request.user.is_authenticated):
            return redirect("home")
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func