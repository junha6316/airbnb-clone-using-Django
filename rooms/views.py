from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

from rooms import models as room_models


# Create your views here.


def all_rooms(request):
    now = datetime.now()

    all_rooms = room_models.Room.objects.all()

    context = {"rooms": all_rooms}
    return render(request, "rooms/all_rooms.html", context=context)
