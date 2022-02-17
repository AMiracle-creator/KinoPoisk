import logging
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse

from kinopoisk.celery import app
from kinopoisk.settings import URL
from main.models import Movie

logger = logging.getLogger(__name__)


@app.task(queue='default')
def movies_count():
    movies = Movie.objects.all()
    logger.info(f'На нашей платформе: {len(movies)} фильмов')
    send_mail("Новые фильмы", "Смотри качественное кино", settings.DEFAULT_FROM_EMAIL,
              [settings.DEFAULT_FROM_EMAIL])


@app.task
def change_password(user_id, token):
    href = URL + reverse('reset_password', kwargs={'user_id': user_id, 'token': token})
    print(href)
    msg = render_to_string('main/reset_email.html', {'href': href})
    send_mail("Привет мир!", "Привет", settings.DEFAULT_FROM_EMAIL,
              [settings.DEFAULT_FROM_EMAIL], html_message=msg)