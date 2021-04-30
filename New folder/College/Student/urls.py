from django.urls import path
from . import views
#student
urlpatterns=[
	path('home/',views.home,name='home'),
	path('register/',views.register,name='register')
]