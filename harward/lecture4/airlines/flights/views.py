from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import *
# Create your views here.
def index(request):
    return render(request,"flights/index.html",{
        "flights": Flight.objects.all()
    })

def flights(request,flight_id):
    f = Flight.objects.get(id=flight_id)
    passengers = f.passengers.all()
    non_passengers = Passenger.objects.exclude(flight_id=f.id)
    return render(request,"flights/flight.html",{
        "flight": Flight.objects.get(id=flight_id),
        "passengers":passengers,
        "nonpassengers":non_passengers
    })

def book(request,flight_id):
    if(request.method=="POST"):
        flight=Flight.objects.get(id=flight_id)
        passenger=Passenger.objects.get(id=int(request.POST["Passenger"]))
        passenger.flight_id.add(flight)
        return HttpResponseRedirect(reverse("flights" ,args=(flight_id,)))
        

# def book(request,):
#     if (request.method == 'POST'):
#         #flight = Flight.objects.get(id=f)
#         return HttpResponse("hello "+request.POST["Passenger"])
#         # passenger = Passenger.objects.get(id=int(request.POST["Passenger"]))
#         # passenger.flight_id.add(flight)
#         # return HttpResponseRedirect(reverse("flight", args=(flight_id,)))

