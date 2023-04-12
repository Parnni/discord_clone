from base import forms
from base.models import Room, Topic
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render


def login_page(request):
    # Redirect to home if the user is already authenticated.
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, f"{username} doesn't exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error("Incorrect credentials are passed")

    context = {}
    return render(request, "base/login_register.html", context)


def logout_page(request):
    logout(request)
    return redirect("home")


def home(request):
    query = request.GET.get("q", "")

    rooms = (
        Room.objects.filter(topic__name__icontains=query)
        if query
        else Room.objects.all()
    )
    rooms_count = rooms.count()
    topics = Topic.objects.all()

    context = {
        "rooms": rooms,
        "rooms_count": rooms_count,
        "topics": topics,
    }
    return render(request, "base/home.html", context)


def room(request, pk):
    context = {"room": Room.objects.get(id=pk)}
    return render(request, "base/room.html", context)


@login_required(login_url="login")
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


@login_required(login_url="login")
def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = forms.RoomForm(instance=room)

    # Only the owner is allowed to make changes.
    if request.user != room.host:
        return HttpResponseBadRequest("Not allowed!")

    # Verifying the posted data.
    if request.method == "POST":
        form = forms.RoomForm(instance=room, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "base/create_room.html", context)


@login_required(login_url="login")
def delete_room(request, pk):
    room = Room.objects.get(id=pk)

    # Only the owner is allowed to make changes.
    if request.user != room.host:
        return HttpResponseBadRequest("Not allowed!")

    if request.method == "POST":
        room.delete()
        return redirect("home")

    context = {"room": room}
    return render(request, "base/delete_room.html", context)
