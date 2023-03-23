from django.shortcuts import render

rooms = [{"id": 1, "name": "Hello"}, {"id": 2, "name": "Ola"}]


def home(request):
    context = {"rooms": rooms}
    return render(request, "base/home.html", context)


def room(request, pk):
    context = {"room": list(filter(lambda room: room["id"] == int(pk), rooms))[0]}
    return render(request, "base/room.html", context)
