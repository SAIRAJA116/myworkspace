from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request,"flights/index.html",{
        "flights":Flight.objects.all()
    })

def flight(request , flight_id):
    flight = Flight.objects.get(id=flight_id)
    return render(request,"flights/flight.html",{
        "flight":flight,
        "passengers":flight.passengers.all(),
        "np":Passenger.objects.exclude(flights=flight).all()
    })


def book(request, flight_id):
    if (request.method == 'POST'):
        flight = Flight.objects.get(id=flight_id)
        passenger = Passenger.objects.get(id=int(request.POST["Passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight_id,)))