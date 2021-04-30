from django.urls import path
from . import views
#student
urlpatterns=[
	path('home/',views.home,name='home'),
	path('register/',views.register,name='register'),
	path('show/',views.show,name='show'),
	path('edit/<int:id>',views.edit,name='edit'),
	path('delete/<int:id>',views.delete,name='delete'),
	path('confirm/<int:id>',views.confirm,name='confirm')
]