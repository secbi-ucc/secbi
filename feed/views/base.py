from django.shortcuts import render


def inicio(request):

    return render(request, 'inicio.html')


def sobre(request):

    return render(request, 'sobre.html')
