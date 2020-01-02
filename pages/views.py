from django.shortcuts import render
from .models import Ally


def home_view(request):
    my_context = {}
    return render(request, 'home.html', my_context)


def mission_view(request):
    my_context = {}
    return render(request, 'mission.html', my_context)


def ally_list_view(request):
    allies = Ally.objects.all()
    my_context = {
        'allies': allies
    }
    return render(request, 'ally_list.html', my_context)


def contact_view(request):
    my_context = {}
    return render(request, 'contact.html', my_context)
