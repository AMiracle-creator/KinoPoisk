from main.models import Movie
from main.models.base import BaseModel
from django.db import models


class Comment(BaseModel):
    author = models.ForeignKey('main.KinopoiskUser', on_delete=models.CASCADE, verbose_name='автор')
    text = models.TextField(verbose_name='комментарий')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='фильм')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'



class MovieRating(BaseModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='фильм')
    score = models.IntegerField(verbose_name='балл')


class Review(BaseModel):
    title = models.CharField(max_length=255, verbose_name='заголовок')
    text = models.TextField(verbose_name='текст')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='фильм')
    author = models.ForeignKey('main.KinopoiskUser', on_delete=models.CASCADE, verbose_name='автор')

    class Meta:
        verbose_name = 'Рецензия'
        verbose_name_plural = 'Рецензии'


class Tag(BaseModel):
    name = models.CharField(max_length=255, verbose_name='тег')

    def __str__(self):
        return f'{self.name}'