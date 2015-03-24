from django.shortcuts import render
from foro.models.user import User
from feed.models import Event


def inicio(request):
    miembros_email = User.objects.filter(es_destacado=True)
    miembros_count = User.objects.all().count()
    events = Event.objects.all()
    return render(request, 'inicio.html', {'miembros_email': miembros_email,
                                           'miembros_count': miembros_count,
                                           'events': events})


def sobre(request):
    miembros = User.objects.all().filter(is_administrator=False)

    return render(request, 'sobre.html', {'miembros': miembros})
