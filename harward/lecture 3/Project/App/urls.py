from django.urls  import path
from . import views
urlpatterns = [
    path("",views.fun,name="fun"),
    #path("/<str:n>",views.name,name="name"),
    path("/new",views.new,name="new"),
    path("<str:name>",views.greet,name="greet"),
    path("/practice",views.practice,name="practice")
]