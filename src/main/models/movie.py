from main.models.base import BaseModel
from django.db import models


class Producer(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    career = models.CharField(max_length=255, verbose_name='Карьера')
    birth_date = models.CharField(max_length=255, verbose_name='Дата рождения')
    birth_place = models.CharField(max_length=255, verbose_name='Mесто рождения')
    total_movies = models.CharField(max_length=255, verbose_name='Всего фильмов')
    img = models.ImageField(upload_to='movies_img/')

    class Meta:
        verbose_name = 'Режисер'
        verbose_name_plural = 'Режиссеры'

    def __str__(self):
        return f'{self.name}' + ' ' + f'{self.last_name}'


class Movie(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Название')
    production_year = models.IntegerField(verbose_name='год производства')
    country = models.CharField(max_length=255, verbose_name='страна')
    genre = models.CharField(max_length=255, verbose_name='жанр')
    producer = models.ForeignKey(Producer, on_delete=models.DO_NOTHING, verbose_name='режиссер')
    budget = models.CharField(max_length=255, verbose_name='бюджет')
    world_premiere = models.CharField(max_length=255, verbose_name='мировая примьера')
    img = models.ImageField(upload_to='movies_img/', verbose_name='изображение')
    overview = models.TextField(verbose_name='обзор')
    tag = models.ManyToManyField('main.Tag', blank=True)
    favorite_movies = models.ManyToManyField('main.KinopoiskUser', blank=True)

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return f'{self.name}'
