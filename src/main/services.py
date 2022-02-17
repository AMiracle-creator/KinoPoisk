from django.db.models import F, Count, Q

from main.models import Movie


def method_f():
    return Movie.objects.filter(id__lt=F('production_year')).aggregate(Count('id'))


def method_q():
    return Movie.objects.filter(Q(name__startswith='Аватар') | Q(world_premiere='10 декабря 2009'))


def select():       
    return Movie.objects.select_related('producer').get(id=2)


def prefetch():
    return list(Movie.objects.prefetch_related("producer").all())


def valueList():
    return Movie.objects.values_list('id', 'name')