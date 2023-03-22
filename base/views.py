from django.http import HttpResponse


def home(request):
    return HttpResponse("This is Home!")


def room(request):
    return HttpResponse("This is room")
