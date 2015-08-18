from django.shortcuts import render
from foro.models.user import User
from feed.models import Event
from django.conf import settings
from foro.models.category import Category
from foro.models.topic import Topic


def inicio(request):
    topics = Topic.objects.for_public().filter(is_pinned=False)
    topics_pinned = Topic.objects.filter(category_id=settings.ST_UNCATEGORIZED_CATEGORY_PK,
                                         is_removed=False,
                                         is_pinned=True)
    topics = topics | topics_pinned
    topics = topics.order_by('-is_pinned', '-last_active').select_related('category')
    categories = Category.objects.for_parent()
    miembros_email = User.objects.filter(es_destacado=True).order_by('id')
    miembros_count = User.objects.all().count()
    events = Event.objects.all()
    return render(request, 'inicio.html', {'miembros_email': miembros_email,
                                           'miembros_count': miembros_count,
                                           'events': events,
                                           'categories': categories,
                                           'topics': topics})


def sobre(request):
    miembros = User.objects.all().filter(is_administrator=False)

    return render(request, 'sobre.html', {'miembros': miembros})
