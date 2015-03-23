from django.shortcuts import render
from foro.models.user import User


def inicio(request):
    return render(request, 'inicio.html')


def sobre(request):
    miembros = User.objects.all().filter(is_administrator=False)

    return render(request, 'sobre.html', {'miembros': miembros})


def proyectos(request):

    return render(request, 'proyectos.html')


def agenda(request):

    return render(request, 'agenda.html')
