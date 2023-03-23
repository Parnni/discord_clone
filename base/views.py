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

    # Verifying the data for POST.
    if request.method == "POST":
        form = forms.RoomForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "base/create_room.html", context)
