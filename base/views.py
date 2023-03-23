from base.models import Room
from django.shortcuts import render


def home(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request, "base/home.html", context)


def room(request, pk):
    context = {"room": Room.objects.get(id=pk)}
    return render(request, "base/room.html", context)
