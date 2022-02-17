from main.models.base import BaseModel
from django.db import models


class News(BaseModel):
    title = models.CharField(max_length=255, verbose_name='заголовок')
    text = models.TextField(verbose_name='текст')
    img = models.ImageField(upload_to='news_img/', verbose_name='изображение')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'