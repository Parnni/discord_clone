from base import forms
from base.models import Room
from django.shortcuts import redirect, render


def home(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request, "base/home.html", context)


def room(request, pk):
    context = {"room": Room.objects.get(id=pk)}
    return render(request, "base/room.html", context)


def create_room(request):
    form = forms.RoomForm()

    # Verifying the posted data.
    if request.method == "POST":
        form = forms.RoomForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "base/create_room.html", context)


def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = forms.RoomForm(instance=room)

    # Verifying the posted data.
    if request.method == "POST":
        form = forms.RoomForm(instance=room, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "base/create_room.html", context)


def delete_room(request, pk):
    room = Room.objects.get(id=pk)

    if request.method == "POST":
        room.delete()
        return redirect("home")

    context = {"room": room}
    return render(request, "base/delete_room.html", context)
